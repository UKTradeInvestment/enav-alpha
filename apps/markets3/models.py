from __future__ import unicode_literals
import base64
import datetime

from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField

# SAMPLE DATA
PLATFORM_BRAND_POSITION = (
    ('0', 'Luxury'),
    ('1', 'Mid rage'),
    ('2', 'Discount')
)

LOGISTICS_MODELS = (
    ('0', 'Dropshipping'),
    ('1', 'Warehousing'),
    ('2', 'Other')
)

# SAMPLE DATA
# Pulled from https://en.wikipedia.org/wiki/ISO_639
LISTING_LANGUAGES = (
    ('0', 'English (eng)'),
    ('1', 'Spanish (spa)'),
    ('2', 'Chinese', ('cdo'))
)

BOOLEAN = (
    ('0', 'No'),
    ('1', 'Yes')
)


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        ordering = ('name',)


class Logo(models.Model):
    name = models.CharField(max_length=200)
    _encoded_data = models.TextField()

    def base64_logo(self):
        return self._encoded_data

    def __str__(self):
        return "{0}".format(self.name)


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
    # Image of the marketplace logo
    logo = models.ForeignKey('Logo', null=True, blank=True)
    # Country where the marketplace is based
    country = models.CharField(max_length=200, blank=True, null=True)
    # That countries that have buyers for the marketplace
    countries_served = models.ManyToManyField(Country)
    # Industry standard for product categories.
    product_categories = models.ManyToManyField(ProductCategory)
    # Do they provide local customer services
    local_customer_service = models.CharField(choices=BOOLEAN, max_length=1, blank=0, default=False)
    local_customer_service_notes = models.CharField(max_length=200, blank=True, null=True, verbose_name='notes')
    # Structure of the logistics and fulfillment for the e-marketplace.
    logistics_structure = models.CharField(choices=LOGISTICS_MODELS, max_length=1, null=True, blank=True)
    # Product type
    product_type = models.CharField(choices=PLATFORM_BRAND_POSITION, max_length=1, null=True, blank=True)

    # Uses the field product_categories, for each category provides a demand value
    product_category_demand = models.CommaSeparatedIntegerField(max_length=500, blank=True, null=True)
    # The number of buyers, sellers on a marketplace.
    size = RichTextField(null=True, blank=True)
    # The number of buyers, sellers for a particular product/product category on a marketplace.
    product_category_size = models.CommaSeparatedIntegerField(max_length=10000, blank=True, null=True)
    # Number of users going to the website per day on average.
    web_traffic_to_site = RichTextField(null=True, blank=True)
    # Number of users bouncing from the website per day on average.
    web_traffic_to_bounce = RichTextField(null=True, blank=True)
    # Structure of the fees and costs for sellers on the marketplace.
    fee_pricing_structure = RichTextField(null=True, blank=True)
    # Terms in place for sellers to receive payment from e-marketplace
    payment_terms = RichTextField(null=True, blank=True)
    # Type of support offered to sellers on the e-marketplace.
    seller_support_structure = RichTextField(null=True, blank=True)
    # Translation services offered for communication between buyers and sellers
    # and/or translation of product/marketing material for a site.
    translation_services = RichTextField(null=True, blank=True)
    # Customer service offered to buyers on the e-marketplace
    buyers_customer_service = RichTextField(null=True, blank=True)
    # Details of the merchandising offer and associated costs involved
    # (fe. marketing, feature to bump your product up on listings)
    merchandising_offer_cost = RichTextField(null=True, blank=True)
    # The payment methods for buyers on the e-marketplace. (fe. Card, PayPal)
    payment_methods = RichTextField(null=True, blank=True)
    # Languages offered for listing products on the e-marketplace
    listing_languages = RichTextField(max_length=500, blank=True, null=True)
    # The number of other sellers for a product/product category on the e-marketplace.
    product_visibility = RichTextField(null=True, blank=True)
    # The types of sellers for product/product category on the e-marketplace.
    competitor_comparison = RichTextField(null=True, blank=True)
    # What terms has been negotiated on behalf of UK Businesses by UKTI
    ukti_terms = RichTextField(null=True, blank=True)
    # Marketplace contacts which are supplied from UKTI for sellers.
    contact_details = RichTextField(null=True, blank=True)
    # List of steps a seller needs to go through to sell on the platform.
    shop_analytics = RichTextField(null=True, blank=True)
    # Tailoring options, themes, etc.
    customization = RichTextField(null=True, blank=True)
    # Details of social media integrations
    social_media_integration = RichTextField(null=True, blank=True)
    # Details of product promotion options
    product_promotion_options = RichTextField(null=True, blank=True)
    # Reviews, ratings, etc.
    feedback_system = RichTextField(null=True, blank=True)
    # Revenue of the business
    revenue = RichTextField(null=True, blank=True)
    # Parent company name
    parent_company_name = RichTextField(null=True, blank=True)
    # Platform target market
    platform_target_market = RichTextField(null=True, blank=True)
    # Product feedback system
    product_feedback_system = RichTextField(null=True, blank=True)
    # The application process for signing up
    seller_application_process = RichTextField(null=True, blank=True)
    # The subscription fee of the platform
    subscription_fees = RichTextField(null=True, blank=True)
    # The registration fee of the platform
    registration_fees = RichTextField(null=True, blank=True)
    # Additional operating fees of the platform
    additional_fees = RichTextField(null=True, blank=True)
    # Referral fee of the platform
    referral_fees = RichTextField(null=True, blank=True)
    # Prohibited items of the platform
    prohibited_items = RichTextField(null=True, blank=True)
    # Logistics options
    logistics_options = RichTextField(null=True, blank=True)
    # Local laws related to the countries in which you want to ship to
    local_laws = RichTextField(null=True, blank=True)
    # Platform signup
    platform_signup = RichTextField(null=True, blank=True)
    # General things to consider
    things_to_consider = RichTextField(null=True, blank=True)
    # Platform type eg shopfront or catalogue
    platform_type = models.CharField(max_length=255, null=True, blank=True)

    web_traffic = models.CharField(max_length=30, null=True, blank=True)

    # Misc fields
    misc1 = RichTextField(null=True, blank=True, help_text='')
    misc2 = RichTextField(null=True, blank=True, help_text='')
    misc3 = RichTextField(null=True, blank=True, help_text='')
    misc4 = RichTextField(null=True, blank=True, help_text='')
    misc5 = RichTextField(null=True, blank=True, help_text='')
    misc6 = RichTextField(null=True, blank=True, help_text='')
    misc7 = RichTextField(null=True, blank=True, help_text='')
    misc8 = RichTextField(null=True, blank=True, help_text='')
    misc9 = RichTextField(null=True, blank=True, help_text='')

    misc10 = RichTextField(null=True, blank=True, help_text='Website traffic - grey box1')
    misc11 = RichTextField(null=True, blank=True, help_text='Website traffic - grey box2')
    misc12 = RichTextField(null=True, blank=True, help_text='Website traffic - grey box3')
    misc13 = RichTextField(null=True, blank=True, help_text='Website traffic - grey box4')
    misc14 = RichTextField(null=True, blank=True, help_text='Demographic profile')
    misc15 = RichTextField(null=True, blank=True, help_text='Product upload process')
    misc16 = RichTextField(null=True, blank=True, help_text='Customer support')
    misc17 = RichTextField(null=True, blank=True, help_text='Local return address (Yes/No)')
    misc18 = RichTextField(null=True, blank=True, help_text='Return rates')
    misc19 = RichTextField(null=True, blank=True, help_text='Marketing and merchandising')

    misc20 = RichTextField(null=True, blank=True, help_text='Local incorporation')
    misc21 = RichTextField(null=True, blank=True, help_text='Local bank account')
    misc22 = RichTextField(null=True, blank=True, help_text='Exclusivity')
    misc23 = RichTextField(null=True, blank=True, help_text='Translation')
    misc24 = RichTextField(null=True, blank=True, help_text='Payment time')
    misc25 = RichTextField(null=True, blank=True, help_text='Exchange rate')
    misc26 = RichTextField(null=True, blank=True, help_text='Bond required')
    misc27 = RichTextField(null=True, blank=True, help_text='')
    misc28 = RichTextField(null=True, blank=True, help_text='')
    misc29 = RichTextField(null=True, blank=True, help_text='')

    def __str__(self):
        return "{0} {1}".format(self.country, self.name)

    class Meta:
        ordering = ('country',)


class OldMarket(Market):
    class Meta:
        proxy = True
        verbose_name = "Market - deprecated"
        verbose_name_plural = "Markets - deprecated"
