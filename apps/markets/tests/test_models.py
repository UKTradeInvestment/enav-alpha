from django.test import TestCase
from ..models import Market


class MarketModelTests(TestCase):

    def test_blank_works(self):
        country = "Aus"
        name = "Amazon"
        market = Market(country=country, name=name)
        market.save()
        self.assertEqual("{0} {1}".format(country, name), str(market))
