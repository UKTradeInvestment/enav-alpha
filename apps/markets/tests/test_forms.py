from django.test import TestCase
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Market
from ..forms import (QueryChoiceField, QueryMultipleChoiceField, QueryMultipleCheckboxField, LogoAdminForm)
from . import (create_market, create_logo, load_sample_png)


class QueryChoicesMixinTests(object):

    def test_query_choices_populated(self):
        create_market(name="Amazon")
        create_market(name="Ebay")
        field = self.field(Market, 'name')
        self.assertListEqual(field.choices, [("Amazon", "Amazon"), ("Ebay", "Ebay")])

    def test_query_choices_distinct(self):
        create_market(name="Amazon", country='uk')
        create_market(name="Amazon", country='us')

        name_field = self.field(Market, 'name')
        self.assertListEqual(name_field.choices, [("Amazon", "Amazon")])

        country_field = self.field(Market, 'country')
        self.assertListEqual(country_field.choices, [("uk", "uk"), ("us", "us")])


class QueryChoiceFieldTests(TestCase, QueryChoicesMixinTests):

    field = QueryChoiceField

    def test_query_choices_setup(self):
        field = self.field(Market, 'name')
        self.assertListEqual(field.choices, [])
        self.assertIsInstance(field.widget, forms.widgets.Select)
        self.assertFalse(field.widget.allow_multiple_selected)


class QueryMultipleChoiceFieldTests(TestCase, QueryChoicesMixinTests):

    field = QueryMultipleChoiceField

    def test_query_choices_empty(self):
        field = self.field(Market, 'name')
        self.assertListEqual(field.choices, [])
        self.assertIsInstance(field.widget, forms.widgets.Select)
        self.assertTrue(field.widget.allow_multiple_selected)


class QueryMultipleCheckboxFieldTests(TestCase, QueryChoicesMixinTests):

    field = QueryMultipleCheckboxField

    def test_query_choices_empty(self):
        field = self.field(Market, 'name')
        self.assertListEqual(field.choices, [])
        self.assertIsInstance(field.widget, forms.widgets.CheckboxSelectMultiple)
        self.assertTrue(field.widget.allow_multiple_selected)


class LogoAdminFormTests(TestCase):

    def test_file_validation(self):
        upload_file = load_sample_png()
        post_dict = {'name': 'logo'}
        file_dict = {'logo': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = LogoAdminForm(post_dict, file_dict)
        self.assertTrue(form.is_valid())

    def test_invalid_file(self):
        post_dict = {'name': 'logo'}
        file_dict = {'logo': SimpleUploadedFile("test.png", b'')}
        form = LogoAdminForm(post_dict, file_dict)
        self.assertFalse(form.is_valid())

    def test_invalid_filename(self):
        upload_file = load_sample_png()
        post_dict = {'name': 'logo'}
        file_dict = {'logo': SimpleUploadedFile("test.jpg", upload_file.read())}
        form = LogoAdminForm(post_dict, file_dict)
        self.assertFalse(form.is_valid())
