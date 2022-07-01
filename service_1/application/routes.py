from application import app
from flask import render_template, request, redirect, url_for
import requests
from random import choice

@app.route('/')
def index():
    chapter = requests.get('http://service_2:5000/get_chapter').text
    service = requests.get('http://service_3:5000/get_service').text
    rank = requests.get('http://service_4:5000/get_rank').text
    return render_template('home.html', rank=rank, chapter=chapter, service=service)
