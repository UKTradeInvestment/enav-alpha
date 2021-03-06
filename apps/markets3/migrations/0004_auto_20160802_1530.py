# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets3', '0003_auto_20160802_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='local_customer_service',
            field=models.CharField(blank=True, choices=[(0, 'Yes'), (1, 'No')], default=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='market',
            name='logistics_structure',
            field=models.CharField(blank=True, choices=[('0', 'Dropshipping'), ('1', 'Warehousing'), ('2', 'Other')],
                                   max_length=1, null=True),
        ),
    ]
