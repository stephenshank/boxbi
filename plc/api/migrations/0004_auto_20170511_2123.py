# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170305_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='corrdata',
            name='BFLSplice',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='corrdata',
            name='BFMSplice',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='corrdata',
            name='CEFLSplice',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='corrdata',
            name='CEFMSplice',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='corrdata',
            name='DBSplice',
            field=models.IntegerField(null=True),
        ),
    ]