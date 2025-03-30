from http.client import responses

import httpx
from jsonschema import validate
from core.contracts import CREATE_USER_SCHEME
from core.contracts import UPDATE_USER_SCHEME
import  datetime

base_url = 'https://reqres.in/'
create_user = 'api/users'
update_user = 'api/users/2'

def test_create_user_with_name_and_date():
    body = {
        'name': 'morpheus',
        'job': 'leader'
    }
    response = httpx.post(base_url + create_user, json=body)
    assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATE_USER_SCHEME)
    assert response_json['name'] == body['name']
    assert response_json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

def test_create_user_without_name():
    body = {
        'job': 'leader'
    }
    response = httpx.post(base_url + create_user, json=body)
    assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATE_USER_SCHEME)
    assert response_json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

def test_create_user_without_job():
    body = {
        'name': 'morpheus'
    }
    response = httpx.post(base_url + create_user, json=body)
    assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATE_USER_SCHEME)
    assert response_json['name'] == body['name']
    assert creation_date[0:16] == current_date[0:16]

def test_put_update_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = httpx.put(base_url + update_user, json=body)
    assert response.status_code == 200

    response_json = response.json()
    update_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response_json, UPDATE_USER_SCHEME)
    assert response_json['name'] == body['name']
    assert response_json['job'] == body['job']
    assert update_date[0:16] == current_date[0:16]

def test_patch_update_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = httpx.patch(base_url + update_user, json=body)
    assert response.status_code == 200

    response_json = response.json()
    update_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response_json, UPDATE_USER_SCHEME)
    assert response_json['name'] == body['name']
    assert response_json['job'] == body['job']
    assert update_date[0:16] == current_date[0:16]

def test_delete_user():
    response = httpx.delete(base_url + update_user)
    assert response.status_code == 204





