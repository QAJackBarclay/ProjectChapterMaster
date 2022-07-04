from flask import Flask, url_for
from flask_testing import TestCase
from application import app 
from unittest.mock import patch
import requests_mock


class TestBase(TestCase):
    def create_app(self):
        return app 

class TestService(TestBase):
    def test_service(self):
        with patch('random.choice') as p:
            p.return_value = "10"
            response =self.client.get(url_for('get_service'))
            self.assert200(response)
            self.assertIn(b'10', response.data)