# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 13:53
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0009_auto_20160721_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='additional_fees',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='last_modified',
            field=models.DateTimeField(
                auto_now=True,
                default=datetime.datetime(2016, 7, 22, 13, 53, 48, 890453, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='market',
            name='local_laws',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='parent_company_name',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='platform_signup',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='platform_target_market',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='product_feedback_system',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='prohibited_items',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='referral_fees',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='registration_fees',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='revenue',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='seller_application_process',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='subscription_fees',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='things_to_consider',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='logistics_options',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='listing_languages',
            field=ckeditor.fields.RichTextField(blank=True, max_length=500, null=True),
        )
    ]
