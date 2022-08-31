import logging
from flask import request, jsonify, Blueprint
from src.config.connection_pool_config import ConnectionFactory

alert_api = Blueprint('alert_api', __name__)

connect_factory = ConnectionFactory()


@alert_api.route('/get_alerts', methods=['GET'])
def get_all_alerts():
    try:
        connection = connect_factory.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT ALERT_ID ,NAME ,DESCRIPTION ,QUERY ,CUSTOMER_ID  from Alert")
        emp_data = cursor.fetchall()
        response = jsonify(emp_data)
        response.status_code = 200
        return response
    except Exception as e:
        logging.log(40, e)
    finally:
        cursor.close()
        ConnectionFactory.pool.release(connection)


@alert_api.route('/add_alert', methods=['POST'])
def inset_alert():
    try:
        json_data = request.json
        name = json_data['name']
        description = json_data['description']
        query = json_data['query']
        customer_id = json_data['customer_id']
        connection = connect_factory.get_connection()
        cursor = connection.cursor()
        sql_query = "INSERT INTO ALERT (NAME, DESCRIPTION, QUERY, CUSTOMER_ID) VALUES (:name, :description, " \
                    ":query, " \
                    ":customer_id) "
        bind_data = [name, description, query, int(customer_id)]
        cursor.execute(sql_query, bind_data)
        connection.commit()
        response = jsonify(f"{name} created successfully!")
        response.status_code = 200
        return response
    except KeyError as e:
        logging.log(40, f"Payload doesn't have all the required data, ${e.args} is missing")
        bad_request()
    except Exception as e:
        logging.log(40, str(e))
    finally:
        cursor.close()
        ConnectionFactory.pool.release(connection)


@alert_api.route('/update_alert', methods=['PUT'])
def update_alert():
    try:
        json_data = request.json
        alert_id = json_data['alert_id']
        name = json_data['name']
        description = json_data['description']
        query = json_data['query']
        customer_id = json_data['customer_id']
        connection = connect_factory.get_connection()
        cursor = connection.cursor()
        sql_query = "UPDATE ALERT SET NAME = :name, DESCRIPTION = :description, QUERY = :query, CUSTOMER_ID = " \
                    ":customer_id WHERE ALERT_ID = :alert_id "
        bind_data = [name, description, query, int(customer_id), int(alert_id)]
        cursor.execute(sql_query, bind_data)
        connection.commit()
        response = jsonify(f"{name} updated successfully!")
        response.status_code = 200
        return response
    except KeyError as e:
        logging.log(40, f"Payload doesn't have all the required data, ${e.args} is missing")
        bad_request()
    except Exception as e:
        logging.log(40, str(e))
    finally:
        cursor.close()
        ConnectionFactory.pool.release(connection)


@alert_api.route('/get_alerts_by_customer/<customer_id>', methods=['GET'])
def get_alert_by_customer_id(customer_id):
    try:
        connection = connect_factory.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT ALERT_ID ,NAME ,DESCRIPTION ,QUERY ,CUSTOMER_ID  from Alert where CUSTOMER_ID = "
                       ":customer_id ",
                       [customer_id])
        emp_data = cursor.fetchall()
        response = jsonify(emp_data)
        response.status_code = 200
        return response
    except Exception as e:
        logging.log(40, e)
    finally:
        cursor.close()
        ConnectionFactory.pool.release(connection)


@alert_api.errorhandler(400)
def bad_request():
    message = {
        "status": 400,
        "message": "Bad Request: " + request.url
    }
    response = jsonify(message)
    response.status_code = 400
    return response
