from application import app
from random import randint

@app.route('/get_service', methods=['GET'])
def get_chapter():
    return (random.randint(2, 60))