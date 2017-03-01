from __future__ import unicode_literals

from django.db import models


class PLC(models.Model):
    plc_id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=64)
    tag = models.CharField(max_length=8)


class CorrData(models.Model):
    class Meta:
        get_latest_by = 'datetime'
    
    datetime = models.DateTimeField(auto_now_add=True)
    UTSPWrapPercentage = models.IntegerField(null=True)
    TempLowOpAS = models.IntegerField(null=True)
    TopMoisture1 = models.FloatField(null=True)
    BottomMoisture1 = models.FloatField(null=True)
    TopMoisture2 = models.FloatField(null=True)
    BottomMoisture2 = models.FloatField(null=True)
    Shoe6 = models.IntegerField(null=True)
    Shoe7 = models.IntegerField(null=True)
    Shoe4 = models.IntegerField(null=True)
    Shoe5 = models.IntegerField(null=True)
    Shoe2 = models.IntegerField(null=True)
    Shoe3 = models.IntegerField(null=True)
    Shoe1 = models.IntegerField(null=True)
    Shoe8 = models.IntegerField(null=True)
    Shoe9 = models.IntegerField(null=True)
    TempLinerLowDrBefHP = models.IntegerField(null=True)
    TempUpDrAS = models.IntegerField(null=True)
    TempLowDrAS = models.IntegerField(null=True)
    Shoe10 = models.IntegerField(null=True)
    TempLinerLowOpBefHP = models.IntegerField(null=True)
    LTSPWrapPercentage = models.IntegerField(null=True)
    TempUpOpAS = models.FloatField(null=True)
    MTSPWrapPercentage = models.FloatField(null=True)
    UpperMeterRollGap = models.FloatField(null=True)
    LowerMeterRollGap = models.FloatField(null=True)
    MachineSpeed = models.IntegerField(null=True)
