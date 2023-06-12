from app import app, WEB_API, firestore_API
from flask import jsonify, request, send_file
from flask_cors import CORS
# from firestore_API import get_data, add_data

app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, support_credentials=True)

@app.route('/')
def example():
    return jsonify({'data':'u r ready to go :)'}), 200, {"set-cookie": "example=r u ready to go ?!"}

@app.route('/get', methods=['GET'])
def getRecord():
    result = firestore_API.get_data()
    # id = request.args.get('id')
    return jsonify(result), 200

@app.route('/create', methods=['POST'])
def createRecord():
    record = request.json
    result = firestore_API.add_data(record)
    return jsonify(result), 200

@app.route('/update', methods=['PUT'])
def updateRecord():
    record = request.json
    return jsonify(record), 200