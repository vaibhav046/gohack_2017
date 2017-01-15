# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneypool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('balance', models.IntegerField()),
                ('relationship', models.CharField(max_length=20)),
                ('mail_id', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=50)),
                ('address_2', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('custom_filter', models.IntegerField(null=True, blank=True)),
                ('customer_type', models.IntegerField(null=True, blank=True)),
                ('vendor_type', models.IntegerField(null=True, blank=True)),
                ('card_number', models.IntegerField(null=True, blank=True)),
                ('name_on_card', models.CharField(max_length=100, null=True)),
                ('expiry', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
