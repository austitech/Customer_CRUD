import datetime

from .db import db


class Debt(db.Document):
    owing = db.StringField(required=True)
    amount = db.StringField(required=True)
    date = db.DateField(default=datetime.date.today)
    date_due = db.DateField(required=True)
    isCleared = db.BooleanField()
