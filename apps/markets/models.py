from __future__ import unicode_literals

from django.db import models

import datetime

from django.utils import timezone


# SAMPLE DATA
PLATFORM_BRAND_POSITION = (
    ('0', 'Luxury'),
    ('1', 'mid'),
    ('2', 'discount')
)

# SAMPLE DATA
# Pulled from https://en.wikipedia.org/wiki/ISO_639
LISTING_LANGUAGES = (
    ('0', 'English (eng)'),
    ('1', 'Spanish (spa)'),
    ('2', 'Chinese', ('cdo'))
)


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('name',)


class Market(models.Model):

    # Trading name of the marketplace
    name = models.CharField(max_length=200, null=True)
    # Description of the marketplace suitable for a seller.
    description = models.CharField(max_length=200, null=True)
    # URL of the market
    web_address = models.URLField(max_length=200, blank=True, null=True)
    # Image of the marketplace logo
    logo = models.ImageField(null=True)
    # Country where the marketplace operates
    country = models.CharField(max_length=200, blank=True, null=True)
    # Region where the marketplace operates
    region = models.CharField(max_length=200, blank=True, null=True)
    # Industry standard for product categories.
    product_categories = models.ManyToManyField(ProductCategory)
    # Uses the field product_categories, for each category provides a demand value
    product_category_demand = models.CommaSeparatedIntegerField(max_length=500, blank=True, null=True)
    # The number of buyers, sellers on a marketplace.
    size = models.TextField(null=True)
    # The number of buyers, sellers for a particular product/product category on a marketplace.
    product_category_size = models.CommaSeparatedIntegerField(max_length=10000, blank=True, null=True)
    # Number of users going to the website per day on average.
    web_traffic_to_site = models.BigIntegerField(null=True)
    # Number of users bouncing from the website per day on average.
    web_traffic_to_bounce = models.BigIntegerField(null=True)
    # Structure of the fees and costs for sellers on the marketplace.
    fee_pricing_structure = models.TextField(null=True)
    # Terms in place for sellers to receive payment from e-marketplace
    payment_terms = models.TextField(null=True)
    # Structure of the logistics and fulfillment for the e-marketplace.
    logistics_structure = models.TextField(null=True)
    # Type of support offered to sellers on the e-marketplace.
    seller_support_structure = models.TextField(null=True)
    # Translation services offered for communication between buyers and sellers
    # and/or translation of product/marketing material for a site.
    translation_services = models.TextField(null=True)
    # Customer service offered to buyers on the e-marketplace
    buyers_customer_service = models.TextField(null=True)
    # Details of the merchandising offer and associated costs involved
    # (fe. marketing, feature to bump your product up on listings)
    merchandising_offer_cost = models.TextField(null=True)
    # The payment methods for buyers on the e-marketplace. (fe. Card, PayPal)
    payment_methods = models.TextField(null=True)
    # Languages offered for listing products on the e-marketplace
    listing_languages = models.CharField(max_length=500, blank=True, null=True)
    # The number of other sellers for a product/product category on the e-marketplace.
    product_visibility = models.TextField(null=True)
    # The types of sellers for product/product category on the e-marketplace.
    competitor_comparison = models.TextField(null=True)
    # What terms has been negotiated on behalf of UK Businesses by UKTI
    ukti_terms = models.TextField(null=True)
    # Marketplace contacts which are supplied from UKTI for sellers.
    contact_details = models.TextField(null=True)
    # List of steps a seller needs to go through to sell on the platform.
    shop_analytics = models.TextField(null=True)
    # Tailoring options, themes, etc.
    customization = models.TextField(null=True)
    # Reviews, ratings, etc.
    feedback_system = models.TextField(null=True)

    def __str__(self):
        return "{0} {1}".format(self.country, self.name)

    class Meta:
        ordering = ('country',)
