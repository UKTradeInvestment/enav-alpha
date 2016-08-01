from __future__ import unicode_literals
import base64
import datetime

from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField


class Region(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('-name',)


class Country(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    region = models.ForeignKey(Region)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('-name',)


class Market(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    # Trading name of the marketplace
    name = models.CharField(max_length=200, null=True, blank=True)
    # Description of the marketplace suitable for a seller.
    description = models.CharField(max_length=200, null=True, blank=True)
    # URL of the market
    web_address = models.URLField(max_length=200, blank=True, null=True)
    # Country where the marketplace is based
    country = models.CharField(max_length=200, blank=True, null=True)
    # That countries that have buyers for the marketplace
    countries_served = models.ManyToManyField(Country)

    # Misc fields
    misc1 = RichTextField(null=True, blank=True)
    misc2 = RichTextField(null=True, blank=True)
    misc3 = RichTextField(null=True, blank=True)
    misc4 = RichTextField(null=True, blank=True)
    misc5 = RichTextField(null=True, blank=True)
    misc6 = RichTextField(null=True, blank=True)
    misc7 = RichTextField(null=True, blank=True)
    misc8 = RichTextField(null=True, blank=True)
    misc9 = RichTextField(null=True, blank=True)

    misc10 = RichTextField(null=True, blank=True)
    misc11 = RichTextField(null=True, blank=True)
    misc12 = RichTextField(null=True, blank=True)
    misc13 = RichTextField(null=True, blank=True)
    misc14 = RichTextField(null=True, blank=True)
    misc15 = RichTextField(null=True, blank=True)
    misc16 = RichTextField(null=True, blank=True)
    misc17 = RichTextField(null=True, blank=True)
    misc18 = RichTextField(null=True, blank=True)
    misc19 = RichTextField(null=True, blank=True)

    misc20 = RichTextField(null=True, blank=True)
    misc21 = RichTextField(null=True, blank=True)
    misc22 = RichTextField(null=True, blank=True)
    misc23 = RichTextField(null=True, blank=True)
    misc24 = RichTextField(null=True, blank=True)
    misc25 = RichTextField(null=True, blank=True)
    misc26 = RichTextField(null=True, blank=True)
    misc27 = RichTextField(null=True, blank=True)
    misc28 = RichTextField(null=True, blank=True)
    misc29 = RichTextField(null=True, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.country, self.name)

    class Meta:
        ordering = ('country',)
