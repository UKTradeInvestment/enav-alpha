# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0004_auto_20160715_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='market',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='market_logos'),
        ),
    ]
