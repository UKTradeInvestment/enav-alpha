from apps.markets.forms import ModelFilterForm, QueryMultipleCheckboxField
from apps.markets.models import Market


class RegionChoiceForm(ModelFilterForm):
    class Meta:
        model = Market
        fields = ['region', ]
        query_fields = [('region', QueryMultipleCheckboxField)]
