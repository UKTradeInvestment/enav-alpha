# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets3', '0004_auto_20160802_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='local_customer_service_notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='local_customer_service',
            field=models.CharField(blank=0, choices=[('0', 'No'), ('1', 'Yes')], default=False, max_length=1),
        ),
    ]
