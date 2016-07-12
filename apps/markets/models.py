from __future__ import unicode_literals

from django.db import models

import datetime

from django.utils import timezone


PLATFORM_TYPE_CHOICES = (
    ('0', 'B2B'),
    ('1', 'B2C'),
)


class Market(models.Model):
    # Country (Should this be an enum?)
    country = models.CharField(max_length=200, blank=True)
    # Website
    website = models.URLField(blank=True)
    # Company name
    company_name = models.CharField(max_length=200, blank=True)
    # Parent company
    parent_company_name = models.CharField(max_length=200, blank=True)
    # Product categories
    # TODO
    # Details of goods sold
    goods_sold = models.TextField(blank=True)
    # Brand domestic
    brand_domestic = models.NullBooleanField()
    # Brand international
    brand_international = models.NullBooleanField()
    # Brand own
    brand_own = models.NullBooleanField()
    # Volume of business(Turnover)
    volume_turnover = models.BigIntegerField(null=True)
    # Date of "Volume of business"
    volume_turnover_date = models.DateField(null=True)
    # Currency conversion rate
    turnover_currency_rate = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    # Turnover GBP
    volume_turnover_gbp = models.BigIntegerField(null=True)
    # Date of conversion
    turnover_conversion_date = models.DateField(null=True)
    # Platform
    platform = models.CharField(max_length=1, choices=PLATFORM_TYPE_CHOICES, blank=True)
    # Date Established
    date_established = models.DateField(null=True)
    # Contact details
    # Contact name
    contact_name = models.CharField(max_length=200, blank=True)
    # Contact position
    contact_position = models.CharField(max_length=200, blank=True)
    # Contact email
    contact_email = models.EmailField(blank=True)
    # Contact phone
    contact_phone = models.CharField(max_length=200, blank=True)
    # Contact address
    contact_address = models.TextField(blank=True)
    # Contact other
    contact_other = models.TextField(blank=True)
    # Strategy and recent investments
    strategy_recent_investments = models.TextField(blank=True)
    # Comments and notes
    comments_notes = models.TextField(blank=True)
    # Sources
    sources = models.TextField(blank=True)
    # Seller application process
    seller_application_process = models.TextField(blank=True)
    # Registration fee
    registration_fee = models.IntegerField(null=True)
    # Subscription fee
    subscription_fee = models.IntegerField(null=True)
    # Referral fee
    referral_fee = models.IntegerField(null=True)
    # Additional operating costs
    additional_operating_costs = models.IntegerField(null=True)
    # Shipping and fulfillment details (comma separated maybe?)
    shipping_fulfillment_details = models.TextField(blank=True)
    # Online marketing (comma separated maybe?)
    online_marketing = models.TextField(blank=True)
    # Payment details
    # Payment credit card
    payment_credit_card = models.NullBooleanField()
    # Payment debit card
    payment_debit_card = models.NullBooleanField()
    # Payment cod
    payment_cod = models.NullBooleanField()
    # Payment bank transfer
    payment_bank_transfer = models.NullBooleanField()
    # Payment paypal
    payment_pay_pal = models.NullBooleanField()
    # Payment other
    payment_other = models.TextField(blank=True)
    # Listing language details
    # Listing english
    listing_english = models.NullBooleanField()
    # Listing local
    listing_local = models.NullBooleanField()
    # Logistics details
    # Logistic full
    logistic_full = models.NullBooleanField()
    # Logistics partial
    logistic_partial = models.NullBooleanField()
    # Logistic DIY
    logistic_diy = models.NullBooleanField()
    # Position in the market
    # Premium
    position_premium = models.NullBooleanField()
    # Midpoint
    position_midpoint = models.NullBooleanField()
    # Discount
    position_discount = models.NullBooleanField()

    def __str__(self):
        return "{0} {1}".format(self.country, self.company_name)

    class Meta:
        ordering = ('country',)
