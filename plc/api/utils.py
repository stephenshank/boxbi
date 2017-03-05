from pycomm.ab_comm.slc import Driver as SlcDriver

from api.models import PLC


ip = '192.168.101.99'
tags = {plc.plc_id: plc.tag for plc in PLC.objects.all()}

def get_plc_data():
    c = SlcDriver()
    states = {}
    if c.open(ip):
        for key, value in tags.iteritems():
            try:
                states[key] = c.read_tag(value)
            except:
                states[key] = None
    return states
