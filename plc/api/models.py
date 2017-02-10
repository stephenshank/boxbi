from __future__ import unicode_literals

from django.db import models


class IP(models.Model):
    ip_id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=64)
    address = models.CharField(max_length=16)

    def __str__(self):
        return self.ip_id


class PLC(models.Model):
    plc_id = models.CharField(primary_key=True, max_length=32)
    ip = models.ForeignKey(IP)
    name = models.CharField(max_length=64)
    tag = models.CharField(max_length=8)
