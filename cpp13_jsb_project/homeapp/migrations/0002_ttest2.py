# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TTest2',
            fields=[
                ('guid', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('rname', models.CharField(max_length=50, null=True)),
                ('pguid', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
