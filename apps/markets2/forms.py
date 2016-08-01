from apps.core.forms import ModelFilterForm, QueryMultipleCheckboxField
from .models import Market


class MarketFilterForm(ModelFilterForm):

    class Meta:
        model = Market
        fields = ['name', ]


class RegionChoiceForm(ModelFilterForm):
    class Meta:
        model = Market
        fields = []
        query_fields = [('countries_served__region__name', QueryMultipleCheckboxField)]
