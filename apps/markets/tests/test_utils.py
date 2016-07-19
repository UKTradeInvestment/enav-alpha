import unittest
from ..templatetags.utils import breadcrumblink


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
