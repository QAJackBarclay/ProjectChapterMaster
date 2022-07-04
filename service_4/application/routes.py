from application import app
from flask import request, Response
import random

@app.route('/get_rank', methods=['POST'])
def get_rank():
    rank = 0
    data = request.get_json()
    
    #Chapters
    if data['chapter'] == 'Dark Angels':
        rank += 10
    if data['chapter'] == 'Ultramarines':
        rank += 20
    if data['chapter'] == 'White Scars':
        rank += 30
    if data['chapter'] == 'Space Wolves':
        rank += 40
    if data['chapter'] == 'Blood Angels':
        rank += 50
    if data['chapter'] == 'Salamanders':
        rank += 60
    if data['chapter'] == 'Imperial Fists':
        rank += 70

    #Service
    if data['service'] == '10':
        rank += 10
    if data['service'] == '20':
        rank += 20
    if data['service'] == '30':
        rank += 30
    if data['service'] == '40':
        rank += 40
    if data['service'] == '50':
        rank += 50
    if data['service'] == '60':
        rank += 60
    if data['service'] == '70':
        rank += 70
    if data['service'] == '80':
        rank += 80
    if data['service'] == '90':
        rank+= 90
    if data['service'] == '100':
        rank += 100
    
    return str(rank)


    