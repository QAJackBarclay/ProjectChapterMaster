from flask import Flask, url_for
from flask_testing import TestCase
from application import app 
from unittest.mock import patch
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app 

class TestChapter(TestBase):
    def test_chapter(self):
        with patch('random.choice') as p:
            p.return_value = "Imperial Fists"
            response =self.client.get(url_for('get_chapter'))
            self.assert200(response)
            self.assertIn(b'', response.data)


class TestChapter(TestBase):
    def test_chapter(self):
        with patch('random.choice') as p:
            p.return_value = "Dark Angels"
            response =self.client.get(url_for('get_chapter'))
            self.assert200(response)
            self.assertIn(b'', response.data)

class TestChapter(TestBase):
    def test_chapter(self):
        with patch('random.choice') as p:
            p.return_value = "Salamanders"
            response =self.client.get(url_for('get_chapter'))
            self.assert200(response)
            self.assertIn(b'', response.data)

class TestChapter(TestBase):
    def test_chapter(self):
        with patch('random.choice') as p:
            p.return_value = "Blood Angels"
            response =self.client.get(url_for('get_chapter'))
            self.assert200(response)
            self.assertIn(b'', response.data)