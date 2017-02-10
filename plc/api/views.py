from django.http import JsonResponse
from pycomm.ab_comm.slc import Driver as SlcDriver

from api.models import PLC


def test(request):
    return JsonResponse({'status': 1})


def plc(request):
    plcs = PLC.objects.filter(ip='db')
    ip_address = plcs[0].ip.address
    tags = {plc.plc_id: plc.tag for plc in plcs}
    return JsonResponse(tags)
    # c = SlcDriver()
    # states = {}
    # if c.open(ip_address):
    #     for key, value in tags.iteritems():
    #         try:
    #             states[key] = c.read_tag(value)
    #         except:
    #             states[key] = ''
    # return JsonResponse(states)
