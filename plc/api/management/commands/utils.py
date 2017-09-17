import datetime as dt
from time import sleep
from traceback import format_exc as format_exception

from django.core.management.base import BaseCommand

from api.models import CorrData, SpliceAtom 


def load_splice_speed():
    atom_query = SpliceAtom.objects.filter(
        SpeedAtSplice=None
    )
    total = len(atom_query)
    print 'Obtained %d atoms...' % total
    for i, atom in enumerate(atom_query):
        corr_query = CorrData.objects.only('MachineSpeed').filter(
            datetime__gte=atom.Datetime
        )[0]
        atom.SpeedAtSplice = corr_query.MachineSpeed
        atom.save()
        print 'Loaded atom %d of %d...' % (i+1, total)

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--task',
            dest='task',
            default=None,
            help='Task to perform. Choice: splicespeed.',
        )

    def handle(self, *args, **options):
        if options['task'] == 'splicespeed':
            print 'Loading speed into splice atoms...'
            load_splice_speed()
            print '...done adding speed information to atoms!'
        else:
            print 'Need to specify a task!'
