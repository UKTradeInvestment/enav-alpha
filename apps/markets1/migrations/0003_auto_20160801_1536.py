# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets1', '0002_auto_20160801_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='market',
            options={'ordering': ('name',)},
        ),
    ]