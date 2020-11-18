import json

import jsonschema
import requests


def get_obj_from_uri(uri, params=None) -> (int, json):
    response = requests.get(uri, params=params)
    return response.status_code, response.json()


def check_json_schema(obj, filename) -> bool:
    with open(filename, 'r') as f:
        schema = json.load(f)
    try:
        jsonschema.validate(obj, schema)
    except jsonschema.ValidationError:
        return False
    return True


def post_obj_from_uri(uri, obj) -> (int, json):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(uri, json=obj,  headers=headers)
    return response.status_code, response.json()


def put_obj_from_uri(uri, obj) -> (int, json):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(uri, json=obj,  headers=headers)
    return response.status_code, response.json()


def patch_obj_from_uri(uri, obj) -> (int, json):
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(uri, json=obj,  headers=headers)
    return response.status_code, response.json()


def delete_obj_from_uri(uri) -> (int, json):
    response = requests.delete(uri)
    return response.status_code, response.json()
