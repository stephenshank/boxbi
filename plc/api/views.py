import json
import os

from django.http import JsonResponse
from pycomm.ab_comm.slc import Driver as SlcDriver
import pyodbc

from api.models import PLC


def test(request):
    return JsonResponse({'status': 1})


def plc(request, ip):
    plcs = PLC.objects.filter(ip=ip)
    ip_address = plcs[0].ip.address
    tags = {plc.plc_id: plc.tag for plc in plcs}
    c = SlcDriver()
    states = {}
    if c.open(ip_address):
        for key, value in tags.iteritems():
            try:
                states[key] = c.read_tag(value)
            except:
                states[key] = ''
    return JsonResponse(states)


def odbc(request):
    odbc_path = os.path.join('data', 'odbc.txt')
    with open(odbc_path, 'r') as odbc_file:
        connection_string = odbc_file.read()
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    order_query = '''SELECT o.QTY_ORDERED, c.CSNAME
                     FROM ORDERS AS o
                     JOIN CUSTOMER AS c
                     ON o.CSCODE = c.CSCODE
                     WHERE o.ORDER_NO=%s''' % request.GET['OrderNumber']
    cursor.execute(order_query)
    result = cursor.fetchone()
    order_info = {
        'QuantityOrdered': result[0],
        'CustomeName': result[1]
    }

    roll_info = {}
    number_of_rolls = request.GET['NumberOfRolls']
    for i in range(int(number_of_rolls)):
        roll_number = request.GET['RollNumber%d' % (i+1)]
        roll_query = '''SELECT i.INVBITEMNO, i.ITEM_WEIGHT, i.RS_LF, v.VNNAME
                        FROM INVENTORY_BIN as i
                        JOIN VENDOR as v
                        ON i.VNCODE = v.VNCODE
                        WHERE i.INVBBINNO='ROLLSTOCK'
                        AND i.RS_VENDOR_ROLL_NO='%s';''' % roll_number
        cursor.execute(roll_query)
        result = cursor.fetchone()
        roll_info[roll_number] = {
            'Info': result[0],
            'Weight': float(result[1]),
            'Lineal': float(result[2]),
            'Vendor': result[3]
        }

    cursor.close()
    connection.close()
    all_info = {'Order': order_info, 'Rolls': roll_info}
    return JsonResponse(all_info)
