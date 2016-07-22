from apps.markets.forms import ModelFilterForm, QueryMultipleCheckboxField
from apps.markets.models import Market, Region


class RegionChoiceForm(ModelFilterForm):
    class Meta:
        model = Market
        fields = []
        query_fields = [('countries_served__region__name', QueryMultipleCheckboxField)]


class ProductChoiceForm(ModelFilterForm):
    class Meta:
        model = Market
        fields = ['product_categories', ]
        query_fields = [('product_categories', QueryMultipleCheckboxField)]
