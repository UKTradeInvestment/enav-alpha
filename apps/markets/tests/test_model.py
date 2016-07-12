from django.test import TestCase
from ..models import Market


class MarketModelTests(TestCase):

    def test_blank_works(self):
        country = "Aus"
        company_name = "Amazon"
        market = Market(country=country, company_name=company_name)
        market.save()
        self.assertEqual("{0} {1}".format(country, company_name), str(market))
