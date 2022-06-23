from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pdb
import os

app = Flask(__name__)
app.config[''] = os.getenv("")
app.config[''] = False
db = SQLAlchemy(app)
app.config[''] = os.getenv("")

from application import routes