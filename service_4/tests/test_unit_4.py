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


    #The reason not 100% is ADD MORE HAHAHA YASSS