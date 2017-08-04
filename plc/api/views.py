import json
import os
import datetime as dt

from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from pycomm.ab_comm.slc import Driver as SlcDriver
import pyodbc

from api.utils import get_plc_data
from api.models import PLC, CorrData, Recipe, SpliceAtom


@api_view()
def test(request):
    return Response({'status': 1})


@api_view()
def realtime(request):
    states = get_plc_data()
    return Response(states)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


@api_view()
def odbc(request):
    odbc_path = os.path.join('data', 'odbc.txt')
    with open(odbc_path, 'r') as odbc_file:
        connection_string = odbc_file.read()
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    order_info = {}
    number_of_orders = int(request.GET['NumberOfOrders'])
    for i in range(number_of_orders):
        order_number = request.GET['OrderNumber%d' % (i+1)]
        order_query = '''SELECT o.QTY_ORDERED, c.CSNAME
                         FROM ORDERS AS o
                         JOIN CUSTOMER AS c
                         ON o.CSCODE = c.CSCODE
                         WHERE o.ORDER_NO=%s;''' % order_number
        cursor.execute(order_query)
        result = cursor.fetchone()
        order_info[order_number] = {
            'Position': i,
            'QuantityOrdered': result[0],
            'CustomerName': result[1]
        }

    roll_info = {}
    number_of_rolls = int(request.GET['NumberOfRolls'])
    for i in range(number_of_rolls):
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
            'Position': i,
            'Info': result[0],
            'Weight': float(result[1]),
            'Lineal': float(result[2]),
            'Vendor': result[3]
        }

    cursor.close()
    connection.close()
    all_info = {'Orders': order_info, 'Rolls': roll_info}
    return Response(all_info)


def card(request):
    return render(request, 'api/recipeCard.html')


@api_view(['GET', 'POST'])
def receive_recipe(request):
    try:
        recipe_data = dict(request.data)
        print recipe_data
        recipe_data['CorrDataID_id'] = recipe_data.pop('CorrDataID')
        recipe = Recipe(**recipe_data)
        recipe.save()
        return Response({'status': 1})
    except:
        return Response({'status': -1})


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        depth = 1


@api_view(['GET', 'POST'])
def send_recipe(request):
    try:
        desired_recipe = Recipe.objects.get(RecipeCardTitle=request.data['RecipeCardTitle'])
        serialized_recipe = RecipeSerializer(desired_recipe)
        return Response(serialized_recipe.data)
    except:
        return Response({'status': -1})


def column(request):
    if 'field' in request.GET.keys():
        field = request.GET['field']
    else:
        field = 'MachineSpeed'
    datetime_start_string = request.GET['datetime_start']
    datetime_end_string = request.GET['datetime_end']
    datetime_start = dt.datetime.strptime(datetime_start_string, '%Y-%m-%dT%H:%M:%SZ')
    datetime_end = dt.datetime.strptime(datetime_end_string, '%Y-%m-%dT%H:%M:%SZ')
    entries = CorrData.objects.only('datetime', field).filter(
        datetime__range=[datetime_start, datetime_end]
    ).values('datetime', field)
    return JsonResponse(list(entries), safe=False)


def splice_atom(request):
    atom_datetime_string = request.GET['datetime']
    atom_datetime = dt.datetime.strptime(atom_datetime_string, '%Y-%m-%dT%H:%M:%SZ')
    first_shift_start = atom_datetime.replace(hour=10, minute=30)
    correction = dt.timedelta(hours=25)
    third_shift_end = first_shift_start+correction
    entries = SpliceAtom.objects.filter(
        Datetime__range=[first_shift_start, third_shift_end]
    ).values()
    return JsonResponse(list(entries), safe=False)


def plc(request):
    return JsonResponse(list(PLC.objects.all().values()), safe=False)


def s2(request):
    return render(request, 'api/index.html')

def snapshot(request):
    datetime_string = request.GET['datetime']
    snap = CorrData.objects.filter(datetime__gte=datetime_string).values()[0]
    return JsonResponse(snap)

