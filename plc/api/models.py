from __future__ import unicode_literals
import datetime as dt

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
    DBSplice = models.IntegerField(null=True)
    CEFMSplice = models.IntegerField(null=True)
    CEFLSplice = models.IntegerField(null=True)
    BFMSplice = models.IntegerField(null=True)
    BFLSplice = models.IntegerField(null=True)
    ShearCurrent = models.IntegerField(null=True)
    Shear11P7A = models.IntegerField(null=True)
    Shear7A3P = models.IntegerField(null=True)
    Shear3P11P = models.IntegerField(null=True)


class Recipe(models.Model):
    CorrDataID = models.ForeignKey(CorrData)
    datetime = models.DateTimeField(auto_now_add=True)
    DBRoll = models.CharField(max_length=32, null=True)
    DBRoll_Vendor = models.CharField(max_length=32, null=True)
    DBRoll_FakeWeight = models.FloatField(null=True)
    DBRoll_TagWeight = models.FloatField(null=True)
    SFCERoll = models.CharField(max_length=32, null=True)
    SFCERoll_Vendor = models.CharField(max_length=32, null=True)
    SFCERoll_FakeWeight = models.FloatField(null=True)
    SFCERoll_TagWeight = models.FloatField(null=True)
    INCERoll = models.CharField(max_length=32, null=True)
    INCERoll_Vendor = models.CharField(max_length=32, null=True)
    INCERoll_FakeWeight = models.FloatField(null=True)
    INCERoll_TagWeight = models.FloatField(null=True)
    SFBRoll = models.CharField(max_length=32, null=True)
    SFBRoll_Vendor = models.CharField(max_length=32, null=True)
    SFBRoll_FakeWeight = models.FloatField(null=True)
    SFBRoll_TagWeight = models.FloatField(null=True)
    INBRoll = models.CharField(max_length=32, null=True)
    INBRoll_Vendor = models.CharField(max_length=32, null=True)
    INBRoll_FakeWeight = models.FloatField(null=True)
    INBRoll_TagWeight = models.FloatField(null=True)
    TopOrder = models.CharField(max_length=32, null=True)
    TopOrder_CustomerName = models.CharField(max_length=64, null=True)
    BotOrder = models.CharField(max_length=32, null=True)
    BotOrder_CustomerName = models.CharField(max_length=64, null=True)
    IsLabTest = models.BooleanField(default=False)
    RecipeCardTitle = models.CharField(max_length=64, null=True)


ATOM_CHOICES = (
    ("DBSplice", "Double backer"),
    ("BFLSplice", "B-flute liner"),
    ("BFMSplice", "B-flute medium"),
    ("CEFMSplice", "C/E-flute medium"),
    ("CEFLSplice", "C/E-flute linear"),
)

class SpliceAtom(models.Model):
    Datetime = models.DateTimeField(default=dt.datetime.utcnow)
    AtomType = models.CharField(choices=ATOM_CHOICES, max_length=12)
    Value = models.IntegerField()

