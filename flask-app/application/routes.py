from application import app
from flask import render_template, request, redirect, url_for
import requests
from random import choice

#choice is function provided by random module, given list/tuple/str and
#choosing it three times


#Sends a request to service 2 to import the main random generator.
@app.route('/')
def index():
    chars = requests.get('http://service_2:5000/get_rank').text
    return render_template('home.html', chars = chars)

@app.route('/home', methods=['GET', 'POST'])
def register_1():
     form = User_Name()
     
     if request.method == 'POST':
          user_name = User(name=form.user_name.data)
     
          if user_name == None:
               message = "Please supply your name!"
          else:
               db.session.add(user_name)
               db.session.commit()
               return redirect(url_for("results"))

     return render_template('home.html', form=form)

#Change to Roman Numerals
@app.route('/get_chapter', methods=['GET'])
def get_chapter_heretic():
    chapter_type = random.choice = ' '
    text = (choice(heretic))

def get_chapter_loyalist():
    chapter_type = random.choice = ' '
    text = (choice(loyalist))
    return render_template('get_rank.html', text)
    
    
@app.route('/get_rank', methods=['GET', 'POST'])
def rank():
     rank_type = random.choice(["Captain", "Chaplain", "Brother", "Scout"])
     return render_template('get_rank.html')

##@app.routes('/get_rank', methods=['GET'])
##def get_rank():
    #rank = 'Scout', 'Brother', 'Captain', 'Chapter Master '
    #text = (choice(rank))
    #return text