
from .db import db


class Customer(db.Document):
    firstname = db.StringField(max_length=50)
    lastname = db.StringField(max_length=50)
    email = db.StringField(required=True)

    def __str__(self):
        return "<Customer: {}>".format(self.firstname)
