
from flask_testing import TestCase
from flask import url_for
from requests_mock import mock
from service_1.application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            rank = requests.get('http://service_2:5000/get_rank').text
            chapter = requests.get('http://service_3:5000/get_chapter').text
            service = requests.post('http://service_4:5000/get_service').int

            response = self.client.get(url_for('home'))

            