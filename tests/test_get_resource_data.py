import httpx
from jsonschema import validate

from core.contracts import LIST_DATA_SCHEME

base_url = 'https://reqres.in/'
list_resource = 'api/unknown'
single_resource = 'api/unknown/2'
not_found_resource = 'api/unknown/23'

def test_list_resource():
    response = httpx.get(base_url + list_resource)
    assert response.status_code == 200

    data_list_resources = response.json()['data']
    for item in data_list_resources:
        validate(item, LIST_DATA_SCHEME)

def test_single_resource():
    response = httpx.get(base_url + single_resource)
    assert  response.status_code == 200

def test_not_found_resource():
    response = httpx.get(base_url + not_found_resource)
    assert  response.status_code == 404
    assert  response.json() == {} # проверка на пустой словарь