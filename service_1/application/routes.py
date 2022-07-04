from application import app
from flask import render_template, request
import requests
from random import choice

@app.route('/')
def index():
    chapter = requests.get('http://service_2:5000/get_chapter').text
    service = requests.get('http://service_3:5000/get_service').text
    rank = requests.post('http://service_4:5000/get_rank',json={'chapter':chapter, 'service':service})
    return render_template('home.html', rank=rank.text, chapter=chapter, service=service)
