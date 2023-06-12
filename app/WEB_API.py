import os
import requests
import json

SERVERURL = os.getenv('SERVERURL')

def get_example():
    res = requests.get(SERVERURL+'/example?args=args')
    results = res.json()
    return results

def post_example():
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({'data': 'example'})
    res = requests.post(SERVERURL+'/example', headers=headers, data=payload)
    results = res.json()
    return results