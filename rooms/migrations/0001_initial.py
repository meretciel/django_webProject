# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_type', models.CharField(max_length=30, choices=[(b'living', b'living room'), (b'bedroom_1', b'master bedroom'), (b'bedroom_2', b'bedroom'), (b'bedroom_3', b'small bedroom')])),
                ('building_name', models.CharField(max_length=40)),
                ('area', models.CharField(max_length=40)),
                ('start_date', models.DateField()),
                ('lease_term', models.IntegerField()),
                ('rent', models.FloatField()),
                ('security_deposit', models.FloatField()),
                ('is_available', models.BooleanField()),
                ('sex', models.CharField(default=b'mixed', max_length=10, choices=[(b'girl', b'girl only'), (b'boy', b'boy only'), (b'mixed', b'boy/girl')])),
            ],
        ),
    ]
