from application import app
import random
from flask import Flask, Response

@app.route('/get_service', methods=['GET'])
def get_service():
    service = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
    selection = random.choice(service)
    return Response(selection, mimetype='text/plain')