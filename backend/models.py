<<<<<<< HEAD
from database import db

class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    place = db.Column(db.String(100))
    category = db.Column(db.String(100))

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100))
=======
from database import db

class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    place = db.Column(db.String(100))
    category = db.Column(db.String(100))

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100))
>>>>>>> 56e814f15d8c66ed8a42f98983505eb945d62847
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'))