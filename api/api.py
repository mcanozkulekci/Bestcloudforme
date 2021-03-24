import flask
from flask import request,jsonify,Response,abort
import json
import logging
import requests
import os

app = flask.Flask(__name__)
url = os.getenv('URL_WHOOK')


data = {'firstname': 'mehmetcan',
        'lastname': 'ozkulekci'}



@app.route('/', methods=['GET'])
def home():
    return "Hello, my name is Mehmet Can Özkülekçi"


@app.route('/whoami',methods=['GET'])
def whoami():
    if request.method == 'GET':
        data["firstname"] = request.args.get('firstname')
        data["lastname"] = request.args.get('lastname')
        return jsonify(data)

@app.route('/alert',methods=['POST'])
def alert():
    if request.method == 'POST':
        print(request.json)
        request_data = request.get_json()
        data = request_data
        r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
