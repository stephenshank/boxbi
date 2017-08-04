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
            raw_atom_data = iter(CorrData.objects.only('datetime', 'DBSplice', 'BFLSplice', 'BFMSplice', 'CEFLSplice', 'CEFMSplice').filter(datetime__gte=dt.date(2017, 7, 5)).values())
            previous_row = next(raw_atom_data)
            for row in raw_atom_data:
                for event_type in ['DBSplice', 'BFLSplice', 'BFMSplice', 'CEFLSplice', 'CEFMSplice']:
                    if row[event_type] != previous_row[event_type]:
                        try:
                            SpliceAtom.objects.create(
                                Datetime=row['datetime'],
                                AtomType=event_type,
                                Value=row[event_type]
                            )
                        except:
                            print 'error inserting row!' + str(row)
                previous_row = row
