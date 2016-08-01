from django.contrib import admin


from .models import Market, Region, Country

admin.site.register(Market)
admin.site.register(Region)
admin.site.register(Country)
