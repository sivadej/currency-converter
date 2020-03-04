from app import app
from session_validator import validate_data, make_uppercase_and_decimal
from currency_converter import get_converted_amount, get_conversion_msg, get_result_msg
from decimal import *
import unittest

class ValidatorTestCase(unittest.TestCase):
    def test_input_formatter(self):
        self.assertEqual(make_uppercase_and_decimal(
            {'convert_from':'gbp', 'convert_to':'GBP', 'amount':0.1}),
            {'convert_from':'GBP', 'convert_to':'GBP', 'amount':Decimal(0.1)})
        self.assertEqual(make_uppercase_and_decimal(
            {'convert_from':'xx', 'convert_to':'Usd', 'amount':'9'}),
            {'convert_from':'XX', 'convert_to':'USD', 'amount':Decimal(9.0)})
        self.assertEqual(make_uppercase_and_decimal(
            {'convert_from':'xx', 'convert_to':'Usd', 'amount':'0'}),
            {'convert_from':'XX', 'convert_to':'USD', 'amount':Decimal(0.0)})
            
    def test_validate_ok(self):
        self.assertTrue(validate_data({'convert_from':'USD', 'convert_to':'GBP', 'amount':Decimal(1)}))
        self.assertTrue(validate_data({'convert_from':'GBP', 'convert_to':'USD', 'amount':Decimal(99.99)}))
    
    def test_validation_messages(self):
        with app.test_client() as client:
            resp = client.post('/convert', follow_redirects=True, data={'convert-from': 'X', 'convert-to':'abc','amount':'1'})
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(get_result_msg(),'')
            html = resp.get_data(as_text=True)
            self.assertIn('X is not a valid code.', html)
            self.assertIn('ABC is not a valid code.', html)