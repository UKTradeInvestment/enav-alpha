from django.contrib import admin

from .models import (Market, OldMarket, ProductCategory, Logo, Region, Country)
from .forms import LogoAdminForm


admin.site.register(OldMarket)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(ProductCategory)


class MarketAdmin(admin.ModelAdmin):
    list_display = ['name', 'web_address']
    ordering = ['name']

    fields = [
        ('name', 'logo',),
        'description',
        'web_address',
        'countries_served',
        'product_categories',
        'logistics_structure',
        ('platform_type', 'product_type'),
        'prohibited_items',
        'local_laws',
        'things_to_consider',
        'ukti_terms',
        'additional_fees',
        'referral_fees',
        'registration_fees',
        'misc10',
        'misc11',
        'misc12',
        'misc13',
        'misc14',
        'misc15',
        'misc16',
        'misc17',
        'misc18',
        'misc19',
        'misc20',
        'misc21',
        'misc22',
        'misc23',
        'misc24',
        'misc25',
        'misc26',
    ]


class LogoAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    form = LogoAdminForm


admin.site.register(Market, MarketAdmin)
admin.site.register(Logo, LogoAdmin)
