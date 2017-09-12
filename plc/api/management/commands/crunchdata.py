import datetime as dt
from time import sleep
from traceback import format_exc as format_exception

from django.core.management.base import BaseCommand

from api.models import CorrData, SpliceAtom 


def update_atoms():
    print 'Grabbing atoms to update...'
    current_time = dt.datetime.utcnow()
    offset = dt.timedelta(minutes=2)
    cutoff = current_time-offset
    atoms = SpliceAtom.objects.filter(Datetime__lte=cutoff, MinSpeed=None)
    print '...grabbed %d atoms!' % len(atoms)
    for i, atom in enumerate(atoms):
        query = CorrData.objects.only('MachineSpeed').filter(
            datetime__gte=atom.Datetime,
            datetime__lte=atom.Datetime+offset
        )
        speeds = [row.MachineSpeed for row in query]
        atom.MinSpeed = min(speeds)
        print 'Saved %d of %d...' % (i+1, len(atoms))
        atom.save()
    print '...done loading atoms!'

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--mode',
            dest='mode',
            default='perpetual',
            help='Mode to run in. Choices: once, perpetual (default).',
        )

    def handle(self, *args, **options):
        if options['mode'] == 'once':
            update_atoms()
        elif options['mode'] == 'perpetual':
            update_atoms()
            while True:
                sleep(5*60)
                update_atoms()
