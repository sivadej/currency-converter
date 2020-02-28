from currency_converter import *
import unittest


class TestConversion(unittest.TestCase):
    def test_currency_conv(self):
        self.assertEqual(get_converted_amount('USD', 'USD', 1), 1)
        self.assertEqual(get_converted_amount('JPY', 'JPY', 100), 100.00)
        self.assertEqual(get_converted_amount('GBP', 'GBP', 55.0), 55.00)


if __name__ == "__main__":
    unittest.main()
