import json
import os

from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from pycomm.ab_comm.slc import Driver as SlcDriver
import pyodbc

from api.utils import get_plc_data
from api.models import PLC, CorrData, Recipe


@api_view()
def test(request):
    return Response({'status': 1})


@api_view()
def realtime(request):
    states = get_plc_data()
    return Response(states)


class CorrDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrData
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


@api_view()
def plc(request):
    current_state = CorrDataSerializer(CorrData.objects.latest())
    return Response(current_state.data)


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

