from application import app
import random
from flask import Flask, Response

@app.route('/get_service', methods=['GET'])
def get_service():
    service = random.randint(10, 100)
    return Response(service, mimetype='text/plain')