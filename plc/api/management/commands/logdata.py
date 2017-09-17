import datetime
from time import sleep
from traceback import format_exc as format_exception

from django.core.management.base import BaseCommand

from api.models import CorrData, SpliceAtom
from api.utils import get_plc_data


class Command(BaseCommand):

    def handle(self, *args, **options):
        splice_tags = [
            'MachineSpeed',
            'DBSplice',
            'BFMSplice',
            'BFLSplice',
            'CEFMSplice',
            'CEFLSplice'
        ]
        old_data = get_plc_data()
        while True:
            sleep(2)
            try:
                # Create all instances
                plc_data = get_plc_data()
                CorrData.objects.create(**plc_data)
                current_time = str(datetime.datetime.now())
                # Create splice related changes
                for splice_tag in splice_tags[1:]:
                    splice_value = plc_data[splice_tag] - old_data[splice_tag]
                    if splice_value != 0:
                        SpliceAtom.objects.create(
                            AtomType=splice_tag,
                            Value=int(splice_value),
                            MinSpeed=None,
                            SpeedAtSplice=plc_data.MachineSpeed
                        )
                        print 'Logged an atom at ' + current_time + '...'
                print 'Logged a sample at ' + current_time + '...'
                old_data = plc_data
            except:
                print format_exception()

