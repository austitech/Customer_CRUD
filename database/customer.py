import datetime

from .db import db

from .transaction import Transaction
from .debt import Debt


class Customer(db.Document):
    id = db.SequenceField(primary_key=True)
    firstname = db.StringField(max_length=50, required=True)
    lastname = db.StringField(max_length=50, required=True)
    email = db.EmailField(required=True, unique=True)
    phone = db.StringField(max_length=15, required=True, unique=True)
    business_name = db.StringField(required=True)
    home_address = db.StringField(required=True)
    reg_date = db.DateField(default=datetime.date.today)
    transactions = db.ReferenceField(Transaction)
    debts = db.ReferenceField(Debt)

    def __str__(self):
        return "<Customer: {}>".format(self.firstname)
