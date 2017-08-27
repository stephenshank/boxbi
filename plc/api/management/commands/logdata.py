from time import sleep
from traceback import format_exc as format_exception

from django.core.management.base import BaseCommand

from api.models import CorrData, StationAtom, ShearAtom
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
        ],
        old_data = get_plc_data()
        while True:
            sleep(2)
            try:
                # Create all instances
                plc_data = get_plc_data()
                CorrData.objects.create(**plc_data)
                
                # Create splice related changes
                for splice_tag in splice_tags[1:]:
                    splice_value = plc_data[splice_tag] - old_data[splice_tag]
                    if splice_value != 0:
                        SpliceAtom.objects.create(
                            AtomType=splice_tag,
                            Value=plc_value,
                            MinSpeed=None
                        )
            except:
                print format_exception()

