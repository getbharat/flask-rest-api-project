from flask import Blueprint
from src.config.connection_pool_config import ConnectionFactory

customer_api = Blueprint('customer_api', __name__)

connection_factory = ConnectionFactory()


@customer_api.route("/add_customer", methods=['POST'])
def add_customer():
    pass


@customer_api.route("/delete_customer", methods=['DELETE'])
def delete_customer():
    pass


@customer_api.route("/delete_customer", methods=['PUT'])
def edit_customer():
    pass


@customer_api.route("/get_customer/<customer_id>", methods=['GET'])
def get_customer_by_id():
    pass


@customer_api.route('/get_all_customers', methods=['GET'])
def get_customer_all_customers():
    pass
