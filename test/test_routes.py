from app import app
from flask import session
#from session_validator import validate_data
#from decimal import *
import unittest

class RoutesTestCase(unittest.TestCase):
    """Tests views rendered at routes"""
    def test_index(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form action="/convert"', html)

    def test_redirect(self):
        with app.test_client() as client:
            resp = client.get('/reset', follow_redirects=True)
            self.assertEqual(resp.status_code, 200)

    def test_valid_session(self):
        with app.test_client() as client:
            with client.session_transaction() as temp_session:
                temp_session['convert_from'] = 'USD'
                temp_session['convert_to'] = 'gbp'
                temp_session['amount'] = 1
            resp = client.get('/')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(session['convert_from'],'USD')
            self.assertEqual(session['convert_to'],'gbp')
            self.assertEqual(session['amount'],1)