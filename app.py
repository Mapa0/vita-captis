from flask import Flask, request
from rich import print
from src.DataCollector import DataCollector, GeographicOperations


app = Flask(__name__)

@app.route('/')
def index():
    return {'Vita-Kod': 'Vita-Captis'}

@app.route('/geo')
def geo():
    body = request.get_json()
    print(body)
    lat = body['lat']
    lng = body['lng']
    go = GeographicOperations()
    return go.get_point_geo_info(lat, lng)

@app.route('/save_data')
def save_data():
    body = request.get_json()
    print(body)
    dc = DataCollector()
    dc.save_report(body)
    return "Salvo"

if __name__ == '__main__':
    app.run()




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
