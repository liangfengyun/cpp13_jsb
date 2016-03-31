# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TTest',
            fields=[
                ('guid', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('uname', models.CharField(max_length=50, null=True)),
                ('upwd', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
