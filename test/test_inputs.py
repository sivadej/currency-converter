from app import app
from currency_converter import *
import unittest

testapp = app.test_client()


class TestInputs(unittest.TestCase):
    def test_validate_inputs(self):
        self.assertTrue(validate_inputs('usd', 'usd', 1))
        self.assertTrue(validate_inputs('gbp', 'GBP', 0.1))
        self.assertTrue(validate_inputs('JPy', 'PHP', 1000.55))
        # self.assertRaises(validate_inputs('xxx', 'USD', Decimal(1.00)))
        # self.assertRaises(validate_inputs('USD', 'xxx', Decimal(1.00)))

    def test_return_incorrect_code(self):
        response = testapp.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
