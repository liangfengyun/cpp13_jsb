# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_ttest2'),
    ]

    operations = [
        migrations.CreateModel(
            name='RTLog_TNote',
            fields=[
                ('guid', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('Log_Guid', models.CharField(max_length=36, null=True)),
                ('Note_Guid', models.CharField(max_length=36, null=True)),
                ('order', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TAccount',
            fields=[
                ('guid', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('openid', models.CharField(max_length=100, null=True)),
                ('nickname', models.CharField(max_length=50, null=True)),
                ('sex', models.NullBooleanField()),
                ('language', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('province', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('headimgurl', models.CharField(max_length=100, null=True)),
                ('subscribe_time', models.DateTimeField(null=True)),
                ('unionid', models.CharField(max_length=100, null=True)),
                ('remark', models.NullBooleanField()),
                ('groupid', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TLog',
            fields=[
                ('guid', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=50, null=True)),
                ('LogDateTime', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TNote',
            fields=[
                ('guid', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('Account_Guid', models.CharField(max_length=36)),
                ('NoteDateTime', models.DateTimeField(null=True)),
                ('Path', models.CharField(max_length=100, null=True)),
                ('Text', models.CharField(max_length=50, null=True)),
                ('NoteType_Guid', models.CharField(max_length=36, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TNoteType',
            fields=[
                ('guid', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('TypeName', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
