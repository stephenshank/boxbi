from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from experiment.models import Experiment, Sample


def mobile(request):
    return render(request, 'experiment/mobile.html')


def desktop(request):
    return render(request, 'experiment/desktop.html')


@api_view()
def initialize(request):
    experiment = Experiment()
    experiment.save()
    experiment_id = experiment.id
    return Response({
        'experiment_id': experiment_id
    })


@api_view(['POST'])
def retrieve(request):
    experiment_id = int(request.data['experiment_id'])
    experiment = Experiment.objects.get(pk=experiment_id)
    return Response({
        'start_time': experiment.start_time
    })


@api_view(['POST'])
def enter(request):
    experiment_id = int(request.data['experiment_id'])
    experiment = Experiment.objects.get(pk=experiment_id)
    for value in filter(None, request.POST.getlist('values[]')):
        sample = Sample(
            experiment=experiment,
            value=float(value)
        )
        sample.save()
    experiment.method = request.data['method']
    experiment.save()
    return Response({
        'status': 1
    })
