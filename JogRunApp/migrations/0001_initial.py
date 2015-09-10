# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JogRunRecord',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('jogrun_date', models.DateField(default=django.utils.timezone.now)),
                ('startline_daytime', models.TimeField(default=django.utils.timezone.now)),
                ('from_stamp', models.CharField(max_length=10)),
                ('to_stamp', models.CharField(max_length=10)),
                ('duration', models.IntegerField(default=0)),
                ('run_length', models.IntegerField(default=0)),
                ('n_of_stops', models.IntegerField(default=0)),
                ('body_natur_weight', models.IntegerField(default=0)),
                ('body_extra_weight', models.IntegerField(default=0)),
                ('weather_type', models.IntegerField(default=0)),
                ('feeling_qualifiers', models.IntegerField(default=0)),
                ('additional_info', models.TextField()),
            ],
        ),
    ]
