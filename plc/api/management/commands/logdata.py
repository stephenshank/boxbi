from time import sleep

from django.core.management.base import BaseCommand

from api.models import DB
from api.utils import get_plc_data


def load_json(filename):
    path = os.path.join('data', filename+'.json')
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data


class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            try:
                plc_data = {key: value or None for key, value in get_plc_data('db').iteritems()}
                DB.objects.create(**plc_data)
            except:
                pass

            sleep(5)
