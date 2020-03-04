from app import app
from currency_converter import *
from session_validator import validate_inputs

import unittest

#testapp = app.test_client()


class TestValidation(unittest.TestCase):

    def test_validate_inputs(self):
        self.assertTrue(validate_inputs('usd', 'usd', 1))
        self.assertTrue(validate_inputs('gbp', 'GBP', 0.1))
        self.assertTrue(validate_inputs('JPy', 'PHP', 1000.55))

    def test_redirect(self):
        with app.test_client() as client:
            response = client.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)