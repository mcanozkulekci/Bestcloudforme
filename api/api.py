import flask
from flask import request,jsonify,url_for


app = flask.Flask(__name__)
app.config["DEBUG"] = True
name ={'firstname': None,
     'lastname': None}



@app.route('/', methods=['GET'])
def home():
    return "Hello, my name is Mehmet Can Özkülekçi"


@app.route('/whoami',methods=['GET'])
def whoami():
    name["firstname"] = request.args.get('firstname')
    name["lastname"] = request.args.get('lastname')

    return jsonify(name)

@app.route('/alert',methods=['POST'])
def alert():
    return jsonify(name)

app.run()