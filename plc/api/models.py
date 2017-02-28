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


class DB(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    UTSPWrapPercentage = models.IntegerField(null=True)
    LTSPCCW = models.IntegerField(null=True)
    UTSPCW = models.IntegerField(null=True)
    TempLowOpAS = models.FloatField(null=True)
    UTSPOver = models.NullBooleanField(null=True)
    Moisture = models.FloatField(null=True)
    LTSPOver = models.NullBooleanField(null=True)
    Shoe6 = models.IntegerField(null=True)
    Shoe7 = models.IntegerField(null=True)
    Shoe4 = models.IntegerField(null=True)
    Shoe5 = models.IntegerField(null=True)
    Shoe2 = models.IntegerField(null=True)
    Shoe3 = models.IntegerField(null=True)
    Shoe1 = models.IntegerField(null=True)
    MTSPCW = models.IntegerField(null=True)
    Shoe8 = models.IntegerField(null=True)
    Shoe9 = models.IntegerField(null=True)
    MTSPOver = models.NullBooleanField(null=True)
    TempLinerLowDrBefHP = models.FloatField(null=True)
    TempUpDrAS = models.FloatField(null=True)
    TempLowDrAS = models.FloatField(null=True)
    LTSPCW = models.IntegerField(null=True)
    Shoe10 = models.IntegerField(null=True)
    MTSPCCW = models.IntegerField(null=True)
    TempLinerLowOpBefHP = models.FloatField(null=True)
    TempLinerUpOpBefGM = models.FloatField(null=True)
    UTSPCCW = models.IntegerField(null=True)
    LTSPWrapPercentage = models.IntegerField(null=True)
    TempUpOpAS = models.FloatField(null=True)
    MTSPWrapPercentage = models.FloatField(null=True)
    TempLinerUpDrBefGM = models.FloatField(null=True)
