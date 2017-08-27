import json
import os
import csv
import datetime as dt

from django.core.management.base import BaseCommand

from api.models import PLC, CorrData, SpliceAtom


def load_json(filename):
    path = os.path.join('data', filename+'.json')
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data


class Command(BaseCommand):

    def handle(self, *args, **options):
        if PLC.objects.count() == 0:
            print 'Loading PLC table...'
            all_plc_data = load_json('plcs')
            plcs = []
            for plc_data in all_plc_data:
                plc = PLC(
                    plc_id=plc_data['id'],
                    name=plc_data['name'],
                    tag=plc_data['tag']
                )
                plcs.append(plc)
            PLC.objects.bulk_create(plcs)
        
        if SpliceAtom.objects.count() == 0:
            print 'Loading SpliceAtom...'
            reader = csv.DictReader(open('data/SpliceAtom.csv'))
            for row in reader:
                SpliceAtom.objects.create(**row)
