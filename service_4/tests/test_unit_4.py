from flask import Flask, url_for
from flask_testing import TestCase
from application import app 
from unittest.mock import patch
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app 

class TestRank(TestBase):
    def test_rank(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Salamanders', 'service':'40'})
        self.assert200(response)
        self.assertIn(b'100', response.data)

class TestRank(TestBase):
    def test_rank(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Dark Angels', 'service':'10'})
        self.assert200(response)
        self.assertIn(b'20', response.data)