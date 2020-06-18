
from flask_restful import Resource
from flask_restful import reqparse

from .database.models import Customer


parser = reqparse.RequestParser()
parser.add_argument('firstname', type=str)
parser.add_argument('lastname', type=str)
parser.add_argument('email', type=str)


class ListCreateCustomer(Resource):
    def post(self):
        data = parser.parse_args()
        Customer(**data).save()

        return {"status": "OK"}, 201

    def get(self):
        customers = Customer.objects().to_json()

        return customers, 200


class GetUpdateDeleteCustomer(Resource):
    def put(self, cust_id):
        data = parser.parse_args()

        Customer.objects.get(id=cust_id).update(**data)

        return {"status": "MODIFIED"}, 203

    def delete(self, cust_id):
        Customer.objects.get(id=cust_id).delete()

        return {"status": "DELETED"}, 200

    def get(self, cust_id):
        customer = Customer.objects.get(id=cust_id)

        return customer, 200
