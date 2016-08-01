from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Market


def create_market(**variable_data):
    if 'name' not in variable_data:
        variable_data['name'] = "Amazon"

    market = Market(**variable_data)
    market.save()
    return market


class MarketModelTests(TestCase):

    def test_blank_works(self):
        name = "Amazon"
        description = "This is a description"
        market = Market(description=description, name=name)
        market.save()
        self.assertEqual(name, str(market))


class MarketListTests(TestCase):

    def test_list_no_markets(self):
        response = self.client.get(reverse('markets1:list'))
        self.assertContains(response, 'No market options are available', status_code=200)

    def test_list_markets(self):
        market = create_market()
        response = self.client.get(reverse('markets1:list'))
        self.assertContains(response, market.name, status_code=200)
