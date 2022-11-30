from flask import Flask, request
from flask_cors import CORS

from rich import print
from os import environ
from src.DataCollector import DataCollector, GeographicOperations


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return {'Vita-Kod': 'Vita-Captis'}

@app.route('/get_reports', methods=['GET'])
def get_reports():
    body = request.get_json()
    if ('limit' in body and 'offset' in body):
        limit = body['limit']
        offset = body['offset']
        dc = DataCollector()
        return dc.get_reports(limit, offset)
    else:
        dc = DataCollector()
        return dc.get_reports()
    
@app.route('/geo', methods=['GET', 'POST'])
def geo():
    body = request.get_json()
    lat = body['lat']
    lng = body['lng']
    go = GeographicOperations()
    return go.get_point_geo_info(lat, lng)

@app.route('/save_data', methods=['GET', 'POST'])
def save_data():
    body = request.get_json()
    dc = DataCollector()
    dc.save_report(body)
    return "Salvo"

if __name__ == '__main__':
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
