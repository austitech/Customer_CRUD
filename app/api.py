
from flask import request

from flask_restful import Resource

from .database.customer import Customer


class ListCreateCustomer(Resource):
    def post(self):
        data = request.get_json(force=True)
        Customer(**data).save()

        return {"status": "OK"}, 201

    def get(self):
        customers = Customer.objects().to_json()

        return customers, 200


class GetUpdateDeleteCustomer(Resource):
    def put(self, cust_id):
        data = request.get_json(force=True)

        Customer.objects.get(id=cust_id).update(**data)

        return {"status": "MODIFIED"}, 203

    def delete(self, cust_id):
        Customer.objects.get(id=cust_id).delete()

        return {"status": "DELETED"}, 200

    def get(self, cust_id):
        customer = Customer.objects.get(id=cust_id).to_json()

        return customer, 200
