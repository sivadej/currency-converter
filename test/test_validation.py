from flask import Flask, redirect, session, request, url_for, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *
import unittest


class TestConversion(unittest.TestCase):
    def test_currency_conv(self):
        """To test return of valid request assuming valid inputs"""
        self.assertEqual(get_converted_amount('USD', 'USD', 1), 1)
        self.assertEqual(get_converted_amount('JPY', 'JPY', 100), 100.00)
        self.assertEqual(get_converted_amount('GBP', 'GBP', 55.0), 55.00)


if __name__ == "__main__":
    unittest.main()
