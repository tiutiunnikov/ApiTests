import json
import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEME
import allure

base_url = 'https://reqres.in/'
register_user = 'api/register'
login_user = 'api/login'

json_file = open('/Users/konstantintiutiunnikov/PycharmProjects/ApiTests/core/new_users_data.json')
users_data = json.load(json_file)

json_file_login = open('/Users/konstantintiutiunnikov/PycharmProjects/ApiTests/core/login_users_data.json')
users_data_login = json.load(json_file_login)

@pytest.mark.parametrize('users_data', users_data)
def test_successful_register(users_data):
    response = httpx.post(base_url + register_user, json=users_data)
    assert  response.status_code == 200

    validate(response.json(), REGISTERED_USER_SCHEME)

@pytest.mark.parametrize('users_data_login', users_data_login)
def test_successful_login(users_data_login):
    response = httpx.post(base_url + login_user, json=users_data_login)
    assert  response.status_code == 200
    assert  'token' in response.json(), "В ответе нет токена"
