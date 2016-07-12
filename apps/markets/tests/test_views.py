from django.test import TestCase
from django.core.urlresolvers import reverse
from ..models import Market


def create_market(**variable_data):
    if 'country' not in variable_data:
        variable_data['country'] = 'uk'
    if 'company_name' not in variable_data:
        variable_data['company_name'] = "Amazon"
    market = Market(**variable_data)
    market.save()
    return market


class MarketListTests(TestCase):

    def test_list_no_markets(self):
        response = self.client.get(reverse('markets:list'))
        self.assertContains(response, 'No market options are available', status_code=200)

    def test_list_markets(self):
        market = create_market()
        response = self.client.get(reverse('markets:list'))
        self.assertContains(response, str(market), status_code=200)


class MarketDetailTests(TestCase):

    def test_detail_market(self):
        market = create_market()
        response = self.client.get(reverse(
            'markets:detail',
            kwargs={'pk': market.pk}))
        self.assertContains(response, str(market), status_code=200)

    def test_detail_404(self):
        response = self.client.get(reverse(
            'markets:detail',
            kwargs={'pk': "123"}))
        self.assertEqual(response.status_code, 404)
