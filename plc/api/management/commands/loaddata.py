import json
import os

from django.core.management.base import BaseCommand

from api.models import IP, PLC


def load_json(filename):
    path = os.path.join('data', filename+'.json')
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data


class Command(BaseCommand):

    def handle(self, *args, **options):
        if IP.objects.count() == 0:
            print('Loading IP table...')
            all_ip_data = load_json('ips')
            ips = []
            for ip_data in all_ip_data:
                ip = IP(
                    ip_id=ip_data['id'],
                    name=ip_data['name'],
                    description=ip_data['description'],
                    address=ip_data['address']
                )
                ips.append(ip)
            IP.objects.bulk_create(ips)

        if PLC.objects.count() == 0:
            print('Loading PLC table...')
            all_plc_data = load_json('plcs')
            plcs = []
            for plc_data in all_plc_data:
                plc = PLC(
                    plc_id=plc_data['id'],
                    ip_id=plc_data['ip'],
                    name=plc_data['name'],
                    tag=plc_data['tag']
                )
                plcs.append(plc)
            PLC.objects.bulk_create(plcs)
