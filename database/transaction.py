import datetime

from .db import db


class Transaction(db.Document):
    date = db.DateField(default=datetime.date.today)
    _from = db.StringField(required=True)
    to = db.StringField(required=True)
    description = db.StringField(required=True)
    payment_method = db.StringField(required=True, default="Cash")
    isCleared = db.BooleanField()

    def __str__(self):
        return "Date: {}".format(self.date)
