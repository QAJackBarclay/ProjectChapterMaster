from application import app
from random import choice
from flask import Response

@app.route('/get_chapter', methods=['GET'])
def get_chapter():  
    choices = ['Dark Angels', 'Imperial Fists', 'Ultramarines', 'White Scars', 'Space Wolves', 'Salamanders', 'Blood Angels' ]
    selection = choice(choices)
    return Response(selection, mimetype='text/plain')

    