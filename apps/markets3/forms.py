from django import forms
from apps.core.forms import ModelFilterForm, QueryMultipleCheckboxField, QueryChoiceField, QueryMultipleChoiceField
from .models import Market, Logo, Region


class MarketFilterForm(ModelFilterForm):

    class Meta:
        model = Market
        fields = ['name', ]
        query_fields = [
            ('name', QueryMultipleCheckboxField),
            ('countries_served__region__name', QueryMultipleCheckboxField),
            ('countries_served__name', QueryMultipleCheckboxField),
            ('platform_type', QueryMultipleCheckboxField),
        ]


class FilteringForm(ModelFilterForm):

    class Meta:
        model = Market
        fields = []
        query_fields = [
            ('platform_type', QueryMultipleCheckboxField),
            ('countries_served__name', QueryChoiceField),
            ('product_categories__name', QueryMultipleChoiceField),
        ]


class LogoAdminForm(forms.ModelForm):

    class Meta:
        model = Logo
        exclude = ['_encoded_data']

    logo = forms.ImageField(label='Upload PNG')

    def clean_logo(self):
        try:
            assert self.files['logo'].name.lower().endswith('.png')
            encoded = "data:image/png;base64,{}".format(
                base64.b64encode(self.files['logo'].read()).decode("utf-8"))
            setattr(self, '_encoded_file_data', encoded)
        except:
            raise forms.ValidationError("Invalid PNG file uploaded.")

    def save(self, *args, **kwargs):
        self.instance._encoded_data = getattr(self, '_encoded_file_data')
        return super(LogoAdminForm, self).save(*args, **kwargs)
