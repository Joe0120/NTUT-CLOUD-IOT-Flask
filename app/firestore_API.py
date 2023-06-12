import os
from google.cloud import firestore
GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
db = firestore.Client(project=GCP_PROJECT_ID)

def add_data(data):
    doc_ref = db.collection('test').document(data['Data']['Measure']['PID'])
    doc_ref.set(data['Data']['Measure'])
    return {'status': 'success'}

def get_data():
    users_ref = db.collection('test')
    docs = users_ref.stream()
    return [doc.to_dict() for doc in docs]