from app import app
from flask import session

from unittest import TestCase
testapp = app.test_client()


class TestViews(unittest.TestCase):
    def test_index(self):
        response = testapp.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_dumb(self):
        self.assertEqual(100, 100)
        self.assertEqual(200, 200)
        self.assertEqual(300, 300)

