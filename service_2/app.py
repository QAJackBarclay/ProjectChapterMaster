from flask import Flask
import random

app = Flask(__name__)

chapter = ['Dark Angels', 'Imperial Fists', 'Ultramarines', 'White Scars', 'Space Wolves']

@app.route('/get_chapter')
def get_rank():
    return random.choice(chapter)

if __name__ == '__main__':
    app.run(host='0.0.0.0')