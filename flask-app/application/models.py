from application import db

class Names(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))

class Chapters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class Legion_Numbers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
