# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneypool', '0004_auto_20170114_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='balance',
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='expiry',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name_on_card',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
