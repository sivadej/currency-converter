from app import app
from flask import session, flash
from currency_converter import get_converted_amount, get_conversion_msg, get_result_msg
import unittest

class ConversionTestCase(unittest.TestCase):
    def test_successful_conversion_result(self):
        with app.test_client() as client:
            with client.session_transaction() as temp_session:
                temp_session['convert_from'] = 'USD'
                temp_session['convert_to'] = 'USD'
                temp_session['amount'] = 1
            resp = client.get('/')
            self.assertEqual(session['convert_from'],'USD')
            self.assertEqual(get_converted_amount(),1.0)
            self.assertEqual(get_result_msg(),'US$ 1.00 = US$ 1.00')

    def test_invalid_code_results(self):
        with app.test_client() as client:
            with client.session_transaction() as temp_session:
                temp_session['convert_from'] = 'X'
                temp_session['convert_to'] = 'USD'
                temp_session['amount'] = 1
            resp = client.get('/')
            self.assertEqual(get_result_msg(),'')