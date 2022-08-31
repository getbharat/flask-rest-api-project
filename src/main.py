from flask import Flask, jsonify
from api.alert import alert_api
from api.customer import customer_api

app = Flask(__name__)
app.register_blueprint(alert_api)
app.register_blueprint(customer_api)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"Status": "Ok"})


if __name__ == '__main__':
    app.run(debug=True)
