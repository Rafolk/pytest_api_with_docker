import pytest
import json
import os
import io
from tests.config.configuration import get_or_update_and_delete_booking_url
from utils.http_methods import HttpMethods


@pytest.fixture(scope='session')
def get_and_create_data():
    script_dir = os.path.dirname(__file__)
    with io.open(os.path.join(script_dir, "get_and_create_data.json"), encoding="utf-8") as json_file:
        return json.load(json_file)

@pytest.fixture(scope='session')
# Вложенная в фикстуру функция для получения существующих параметров запроса
def get_parametrize_value(get_exist_booking_ids):
    link_for_get_current_booking = get_or_update_and_delete_booking_url + str(get_exist_booking_ids(0))
    response = HttpMethods.get(link_for_get_current_booking)
    json_response = response.json()
    bookingdates = json_response.get("bookingdates")
    parametrize_value = {
        "firstname": json_response.get("firstname"),
        "lastname": json_response.get("lastname"),
        "checkin": bookingdates.get("checkin"),
        "checkout": bookingdates.get("checkout")
        }
    return parametrize_value

@pytest.fixture(scope='session')
# Вложенная в фикстуру функция для проверки списка одинаковых ключей и их значений на int
def check_booking_ids():
    def function_check_booking_ids(response):
        json_list = response.json()
        for obj in json_list:
            if "bookingid" in obj:
                if not isinstance(obj["bookingid"], int):
                    return False
            else:
                return False
        return 0
    return function_check_booking_ids


@pytest.fixture(scope='session')
# Вложенная в фикстуру функция для проверки типов данных значений ключей ответа на get-апрос
def check_type_data_key_value():
    def function_check_type_data_key_value(response):
        json_list = response.json()
        assert type(json_list["firstname"]) == str, f'Тип данных значения ключа из ответа ошибочный.'
        assert type(json_list["lastname"]) == str, f'Тип данных значения ключа из ответа ошибочный.'
        assert type(json_list["totalprice"]) == int, f'Тип данных значения ключа из ответа ошибочный.'
        assert type(json_list["depositpaid"]) == bool, f'Тип данных значения ключа из ответа ошибочный.'
        assert type(json_list["bookingdates"]) == dict, f'Тип данных значения ключа из ответа ошибочный.'
        bookingdates_dict = json_list["bookingdates"]
        assert type(bookingdates_dict["checkin"]) == str, f'Тип данных значения ключа из ответа ошибочный.'
        assert type(bookingdates_dict["checkout"]) == str, f'Тип данных значения ключа из ответа ошибочный.'
    return function_check_type_data_key_value
