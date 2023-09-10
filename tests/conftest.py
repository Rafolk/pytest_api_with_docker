import allure
import pytest
import json
from tests.config.configuration import get_all_ids_or_create_booking_url, auth_token_url
from utils.http_methods import HttpMethods


@pytest.fixture(scope='session')
def auth_token_in_cookie():
    auth_data = {
        "username": "admin",
        "password": "password123"
        }
    response = HttpMethods.post(auth_token_url, body=auth_data)
    auth_token = response.json()['token']
    cookies = {
        "token": auth_token
    }
    return cookies

@pytest.fixture(scope='session')
# Фикстура для получения существующего ID
def get_exist_booking_ids():
    def function_get_exist_booking_ids(number):
        response = HttpMethods.get(get_all_ids_or_create_booking_url)
        assert response.status_code == 200, f'Не удалось получить существующий ID, статус-код = {response.status_code}'
        json_list = response.json()
        get_element = json_list[number]
        exist_id = get_element.get("bookingid")
        return exist_id
    return function_get_exist_booking_ids

@pytest.fixture(scope='session')
# Вложенная в фикстуру функция для проверки списка ключей
def check_json_key():
    def function_check_json_key(response, expected_json_key):
        json_key = json.loads(response.text)
        assert json_key is not None and json_key != ""
        assert list(json_key) == expected_json_key, f'Ошибка проверки ключей, {response.text}'
        # Способ получения всех ключей из ответа
        # json_key = json.loads(response.text)
        # print(list(json_key))
    return function_check_json_key

@pytest.fixture(scope='session')
# Вложенная в фикстуру функция для проверки содержимого ключа из json
def check_json_key_value():
    def function_check_json_key_value(response, key_name, expected_json_key_value, check_non_empty=False):
        json_key = json.loads(response.text)
        json_key_value = json_key.get(key_name)
        if check_non_empty:
            assert json_key_value is not None and json_key_value != "", \
                f'Ошибка проверки непустого значения ключа {key_name}, фактическое значение: {json_key_value}'
            return 0
        assert json_key_value == expected_json_key_value, \
                f'Ошибка проверки содержимого ключа {key_name}, фактическое значение: {json_key_value}'
    return function_check_json_key_value
