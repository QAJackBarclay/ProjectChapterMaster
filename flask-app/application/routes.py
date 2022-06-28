from application import app
from flask import render_template
import requests
from random import choice


#Sends a request to service 2 to import the main random generator.
@app.route('/')
def index():
    chars = requests.get('http://service_2:5000/get_rank').text
    return render_template('home.html', chars = chars)

#choice is function provided by random module, given list/tuple/str and
#choosing it three times

#Change to Roman Numerals
@app.routes('/get_rank', methods=['GET'])
def get_rank():
    rank = 'Scout', 'Brother', 'Captain', 'Chapter Master '
    text = (choice(rank))
    return text

#Sends a request to service 2 to import the main random generator.
@app.route('/')
def index():
    chars = requests.get('http://service_2:5000/get_rank').text
    return render_template('home.html', chars = chars)

from application import app, db
from flask import render_template, request, redirect, url_for


@app.route('/home', methods=['GET', 'POST'])
def home():
     return render_template('home.html')

@app.route('/profile')
def index():
     return render_template('profile.html')

@app.route('/generator', methods=['GET', 'POST'])
def rank():
     rank_type = random.choice(["Captain", "Chaplain", "Brother", "Scout"])
     return render_template('generator.html', unit_type)