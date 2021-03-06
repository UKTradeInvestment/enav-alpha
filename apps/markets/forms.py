import base64
from django import forms
from django.db import models

from .models import Market, Logo


class QueryChoiceMixin(object):
    """
    Mixin for a choice field, that takes a model and an attribute of that model, and gets all distinct values for that
    attribute from the database, and uses that to generate the choices of the field
    """

    def __init__(self, model, attr, *args, **kwargs):
        components = attr.split('__')
        attr = components.pop()

        for component in components:
            model = model._meta.get_field(component).related_model

        model_field = model._meta.get_field(attr)
        if isinstance(model_field, models.ManyToManyField):
            related_model = model_field.related_model
            choices = [(model.pk, "{0}".format(model)) for model in related_model.objects.all()]
        elif len(model_field.choices) > 0:
            choices = model_field.choices
        else:
            choices = model.objects.all().values_list(attr, attr).distinct().order_by(attr)

        return super().__init__(choices=choices, required=False, *args, **kwargs)


class QueryChoiceField(QueryChoiceMixin, forms.ChoiceField):
    """
    A convinience model using QueryChoiceMixin and ChoiceField, that provide a ChoiceField that set it's own choices
    """

    pass


class QueryMultipleChoiceField(QueryChoiceMixin, forms.MultipleChoiceField):
    """
    A convinience model using QueryChoiceMixin and MultipleChoiceField, that provide a MultipleChoiceField that set
    it's own choices
    """

    pass


class QueryMultipleCheckboxField(QueryMultipleChoiceField):
    """
    A convinience model identical to the QueryMultipleChoiceField, but that uses a default mutliple checkbox as it's
    widget, rather than a multi-select box
    """

    def __init__(self, *args, **kwargs):
        return super().__init__(widget=forms.CheckboxSelectMultiple(), *args, **kwargs)


class ModelFilterForm(forms.ModelForm):
    """
    A Model form that can have a specified list of query_fields, and it will automatically convert these into
    QueryMultipleCheckboxFields
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            query_fields = self.Meta.query_fields
        except AttributeError:
            query_fields = []

        for field_name, field_type in query_fields:
            self.fields[field_name] = field_type(self.Meta.model, field_name)


class MarketFilterForm(ModelFilterForm):

    class Meta:
        model = Market
        fields = ['name', ]
        query_fields = [
            ('name', QueryMultipleCheckboxField),
            ('countries_served__region__name', QueryMultipleCheckboxField),
            ('countries_served__name', QueryMultipleCheckboxField),
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
