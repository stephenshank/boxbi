# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('stand_number', models.IntegerField()),
                ('rollID', models.CharField(max_length=64)),
                ('side', models.CharField(choices=[(b'left', b'Left side'), (b'right', b'Right side')], max_length=5)),
            ],
        ),
    ]