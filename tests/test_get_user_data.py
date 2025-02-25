import httpx
from jsonschema import validate

from core.contracts import USER_DATA_SCHEME

import allure

base_url = 'https://reqres.in/'
list_users = 'api/users?page=2'
single_user = 'api/users/2'
not_found_user = 'api/users/23'
email_ends = '@reqres.in'
avatar_ends = '-image.jpg'

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверка статуса запроса')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу {base_url + list_users}'):
        response = httpx.get(base_url + list_users)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    data = response.json()['data']
    for item in data:
        with allure.step((f'Проверяем элемент из списка')):
            validate(item, USER_DATA_SCHEME)
        with allure.step('Проверяем окончание E-mail адреса'):
            assert item['email'].endswith(email_ends)
        with allure.step('Проверяем наличие id в ссылке на аватар'):
            assert item['avatar'].endswith(str(item['id']) + avatar_ends)

@allure.suite('Проверка запроса данных одного пользователя')
@allure.title('Проверка статуса запроса одного пользователя')
def test_single_users():
    response = httpx.get(base_url + single_user)
    assert  response.status_code == 200
    data = response.json()['data']

    assert data['email'].endswith(email_ends)
    assert data['avatar'].endswith(str(data['id']) + avatar_ends)

def test_user_not_found():
    response = httpx.get(base_url + not_found_user)
    assert response.status_code == 404


