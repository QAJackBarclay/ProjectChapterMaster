from flask import Flask, url_for
from flask_testing import TestCase
from application import app 
from unittest.mock import patch
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app 

class TestRank(TestBase):
    def test_rank1(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Salamanders', 'service':'40'})
        self.assert200(response)
        self.assertIn(b'100', response.data)

    def test_rank2(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Dark Angels', 'service':'10'})
        self.assert200(response)
        self.assertIn(b'20', response.data)

    def test_rank3(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Blood Angels', 'service':'80'})
        self.assert200(response)
        self.assertIn(b'130', response.data)

    def test_rank4(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Imperial Fists', 'service':'100'})
        self.assert200(response)
        self.assertIn(b'170', response.data)

    def test_rank5(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'White Scars', 'service':'90'})
        self.assert200(response)
        self.assertIn(b'120', response.data)

    def test_rank6(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Blood Angels', 'service':'60'})
        self.assert200(response)
        self.assertIn(b'110', response.data)

    def test_rank7(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Space Wolves', 'service':'70'})
        self.assert200(response)
        self.assertIn(b'110', response.data)

    def test_rank8(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Ultramarines', 'service':'20'})
        self.assert200(response)
        self.assertIn(b'40', response.data)

    def test_rank9(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Ultramarines', 'service':'50'})
        self.assert200(response)
        self.assertIn(b'70', response.data)

    def test_rank10(self):
        response =self.client.post(url_for('get_rank'), json={'chapter':'Imperial Fists', 'service':'30'})
        self.assert200(response)
        self.assertIn(b'100', response.data)