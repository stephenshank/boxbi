from django.http import JsonResponse
from pycomm.ab_comm.slc import Driver as SlcDriver

from api.models import PLC


def test(request):
    return JsonResponse({'status': 1})


def plc(request, ip):
    plcs = PLC.objects.filter(ip=ip)
    ip_address = plcs[0].ip.address
    tags = {plc.plc_id: plc.tag for plc in plcs}
    c = SlcDriver()
    states = {}
    if c.open(ip_address):
        for key, value in tags.iteritems():
            try:
                states[key] = c.read_tag(value)
            except:
                states[key] = ''
    return JsonResponse(states)
