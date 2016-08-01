"""
import unittest
from . import create_market, create_country
from ..templatetags.utils import breadcrumblink, get_regions, get_countries


class TestBreabcrumbs(unittest.TestCase):

    def test_breadcrumblink_one_param(self):
        self.assertEqual(breadcrumblink('region=European', 'region'), 'region=European')

    def test_breadcrumblink_multiple_params_and_querystries(self):
        query1 = 'region=European+Union&product_categories=13'
        query2 = 'region=European+Union&region=Africa&product_categories=13&product_categories=14'
        self.assertEqual(breadcrumblink(query1, 'region', 'product_categories'), query1)
        self.assertEqual(breadcrumblink(query2, 'region', 'product_categories'), query2)

    def test_breadcrumblink_invalid_param_empty_array(self):
        self.assertEqual(breadcrumblink('region=European', ''), '')

    def test_breadcrumblink_invalid_param_string(self):
        self.assertEqual(breadcrumblink('region=European+Union&product_categories=13', 'a'), '')


class TestMarketCountries(unittest.TestCase):

    def test_get_one_country(self):
        market = create_market(country='UK')
        countries = get_countries(market)
        self.assertEqual(countries, "UK")

    def test_get_multiple_countries(self):
        china = create_country('China', 'Asia')
        japan = create_country('UK', 'Europe')
        market = create_market(country='UK', region='Europe', countries_served=[china, japan])
        countries = get_countries(market)
        self.assertEqual(countries, 'China, UK')


class TestMarketRegions(unittest.TestCase):

    def test_get_one_region(self):
        market = create_market(country='UK', region='Europe')
        regions = get_regions(market)
        self.assertEqual(regions, "Europe")

    def test_get_multiple_regions(self):
        china = create_country('China', 'Asia')
        japan = create_country('UK', 'Europe')
        market = create_market(country='UK', region='Europe', countries_served=[china, japan])
        regions = get_regions(market)
        self.assertEqual(regions, 'Asia, Europe')
"""