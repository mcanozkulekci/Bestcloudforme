import flask
from flask import request,jsonify,Response,abort
import json
import logging
import requests
from webhook import data

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return "Hello, my name is Mehmet Can Özkülekçi"


@app.route('/whoami',methods=['GET'])
def whoami():
    data["firstname"] = request.args.get('firstname')
    data["lastname"] = request.args.get('lastname')

    return jsonify(data)

@app.route('/alert',methods=['POST'])
def alert():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
