from application import app
from flask import render_template, request, redirect, url_for
import requests
from random import choice

@app.route('/')
def index():
    rank = requests.get('http://service_2:5000/get_rank').text
    chapter = requests.get('http://service_3:5000/get_chapter').text
    name = requests.post('http://service_4:5000/get_service').int
    return render_template('home.html')
