# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 15:04
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0006_auto_20160720_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='size',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
