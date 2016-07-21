from django.contrib import admin

from .models import (Market, ProductCategory, Logo)
from .forms import LogoAdminForm

admin.site.register(Market)
admin.site.register(ProductCategory)


class LogoAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    form = LogoAdminForm


admin.site.register(Logo, LogoAdmin)
