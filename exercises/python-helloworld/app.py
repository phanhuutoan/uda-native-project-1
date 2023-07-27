from flask import Flask
import json
import logging

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("Hello from app")
    return "Hello World!"


@app.route('/status')
def status():
    response = app.response_class(
        status=200,
        response=json.dump({"status": "OK"}),
        mimetype='application/json'
    )
    return response


@app.route('/metrics')
def metric():
    response = app.response_class(
        status=200,
        response=json.dumps({"status": "success", "code": 0, "data": {
                            "UserCount": 140, "UserCountActive": 23}}),
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    logging.basicConfig(filename='app.logs', level=logging.DEBUG)
    app.run(host='0.0.0.0')
