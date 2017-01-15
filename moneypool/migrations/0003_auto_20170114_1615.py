# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneypool', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterprofile',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
