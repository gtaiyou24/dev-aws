from __future__ import print_function

import flask
import json
from flask import jsonify, request


app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # health = ScoringService.get_model() is not None  # You can insert a health check here
    health = True

    status = 200 if health else 404
    return flask.Response(response='\n', status=status, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def transformation():
    if flask.request.content_type == 'application/json':
        result = json.dumps({
            'first_name': request.json["first_name"],
            'last_name': request.json["last_name"]
        })
        return flask.Response(response=result, status=200, mimetype='application/json')
    else:
        return flask.Response(response='This predictor only supports CSV data', status=415, mimetype='text/plain')