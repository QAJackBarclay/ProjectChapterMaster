from application import app, db
from flask import render_template, request, redirect, url_for


@app.route('/home', methods=['GET', 'POST'])
def home():
     return render_template('home.html')

@app.route('/profile')
def index():
     return render_template('profile.html')

@app.route('/generator')
def index():
     return render_template('generator.html')
