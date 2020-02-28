from app import app
from currency_converter import *
import unittest

testapp = app.test_client()


class TestInputs(unittest.TestCase):
    def test_validate_inputs(self):
        self.assertEqual(validate_inputs('USD', 'USD', Decimal(1.00)), True)
        self.assertRaises(validate_inputs('xxx', 'USD', Decimal(1.00)))
        self.assertRaises(validate_inputs('USD', 'xxx', Decimal(1.00)))

        response = testapp.post('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
