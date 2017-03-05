from time import sleep

from django.core.management.base import BaseCommand

from api.models import CorrData
from api.utils import get_plc_data


class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            try:
                plc_data = get_plc_data()
                CorrData.objects.create(**plc_data)
            except:
                pass

            sleep(5)
