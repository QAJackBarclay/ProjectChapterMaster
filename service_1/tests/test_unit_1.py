from flask import Flask, url_for
from flask_testing import TestCase
from application import app 
from unittest.mock import patch
import requests_mock

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_chapter',text = 'Dark Angels')
            m.get('http://service_3:5000/get_service', text = '20')
            m.post('http://service_4:5000/get_rank', text = '30')
            response=self.client.get(url_for('index'))
            self.assert200(response)
            self.assertIn(b'Dark Angels', response.data)
            self.assertIn(b'20', response.data)
            self.assertIn(b'30', response.data)
            