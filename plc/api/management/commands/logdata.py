from time import sleep
from traceback import format_exc as format_exception

from django.core.management.base import BaseCommand

from api.models import CorrData, StationAtom, ShearAtom
from api.utils import get_plc_data


class Command(BaseCommand):

    def handle(self, *args, **options):
        i = 0
        main_tags = [
            'MachineSpeed',
            'DBSplice',
            'BFMSplice',
            'BFLSplice',
            'CEFMSplice',
            'CEFLSplice'
        ],
        shear_tags = [
            'ShearCurrent',
            'Shear11P7A',
            'Shear7A3P',
            'Shear3P11P '
        ]
        plc_data = get_plc_data()
        main_data = {tag: plc_data[tag] for tag in main_tags}
        shear_data = {tag: plc_data[tag] for tag in shear_tags}
        while True:
            sleep(2)
            try:
                # Create all instances
                plc_data = get_plc_data()
                CorrData.objects.create(**plc_data)
                
                # Create speed related changes
                if main_data['MachineSpeed'] > 450 and plc_data['MachineSpeed'] <= 450:
                    SpliceAtom.objects.create(
                        AtomType='MachineSlow',
                        Value=0
                    )
                elif main_data['MachineSpeed'] > 0 and plc_data['MachineSpeed'] == 0:
                    SpliceAtom.objects.create(
                        AtomType='MachineStop',
                        Value=0
                    )
                elif main_data['MachineSpeed'] == 0 and plc_data['MachineSpeed'] >= 0:
                    SpliceAtom.objects.create(
                        AtomType='MachineStop',
                        Value=1
                    )
                elif main_data['MachineSpeed'] < 450 and plc_data['MachineSpeed'] >= 450:
                    SpliceAtom.objects.create(
                        AtomType='MachineSlow',
                        Value=1
                    )


                # Create splice related changes
                for splice_tag in main_tags[1:]:
                    splice_value = plc_data[splice_tag]
                    if main_data[splice_tag] != plc_value:
                        SpliceAtom.objects.create(
                            AtomType=splice_tag,
                            Value=plc_value
                        )
                        main_data[splice_tag] = plc_value
                i += 1
                if i == 30:
                    i = 0
                    for shear_tag in shear_tags:
                        plc_value = plc_data[shear_tag]
                        if shear_data[shear_tag] != plc_value:
                            ShearAtom.objects.create(
                                Value=plc_value
                            )
                            shear_data[shear_tag] = plc_value
            except:
                print format_exception()

