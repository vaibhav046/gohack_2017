# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneypool', '0003_auto_20170114_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('from_user', models.IntegerField()),
                ('to_user', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('transaction_id', models.AutoField(serialize=False, primary_key=True)),
                ('group_id', models.IntegerField()),
                ('timestamp', models.CharField(max_length=100)),
                ('transaction_type', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='masterprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='masterprofile',
            name='group_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
