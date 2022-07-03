from sqlalchemy import null
from . import db
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SelectField


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    phone_no = db.Column(db.String(20))
    floor = db.Column(db.Integer)
    company = db.Column(db.String(40))
    whom_to_see = db.Column(db.String(40))
    comment = db.Column(db.String(1500))
    date_in = db.Column(db.DateTime, default=datetime.utcnow)
    time_out = db.Column(db.DateTime, default=datetime.utcnow)
