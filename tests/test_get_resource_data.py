import httpx
from jsonschema import validate
from core.contracts import LIST_DATA_SCHEME
import allure

base_url = 'https://reqres.in/'
list_resource = 'api/unknown'
single_resource = 'api/unknown/2'
not_found_resource = 'api/unknown/23'

@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение списка ресурсов')
def test_list_resource():
    with allure.step(f'Делаем запрос по адресу: {base_url + list_resource}'):
        response = httpx.get(base_url + list_resource)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    data_list_resources = response.json()['data']
    for item in data_list_resources:
        with allure.step('Проверяем структуру ответа'):
            validate(item, LIST_DATA_SCHEME)

@allure.suite('Проверка запросов данных одного ресурса')
@allure.title('Проверяем код ответа одного ресурса')
def test_single_resource():
    with allure.step(f'Делаем запрос по адресу: {base_url + single_resource} '):
        response = httpx.get(base_url + single_resource)
    with allure.step('Проверяем код ответа'):
        assert  response.status_code == 200

@allure.suite('Проверка запросов ненайденного ресурса')
@allure.title('Проверяем код ответа ненайденного ресурса')
def test_not_found_resource():
    with allure.step(f'Делаем запрос по адресу: {base_url + not_found_resource}'):
        response = httpx.get(base_url + not_found_resource)
    with allure.step('Проверяем код ответа ненайденного ресурса'):
        assert  response.status_code == 404
    with allure.step('Проверка на пустой словарь'):
        assert  response.json() == {} # проверка на пустой словарь