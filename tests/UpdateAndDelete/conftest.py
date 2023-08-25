import pytest
import json
import os
import io


@pytest.fixture(scope='session')
def update_and_delete_data():
    script_dir = os.path.dirname(__file__)
    with io.open(os.path.join(script_dir, "update_and_delete_data.json"), encoding="utf-8") as json_file:
        return json.load(json_file)

@pytest.fixture(scope='session')
# Фикстура для проверки частичного обновления
def check_partial_update():
    def function_check_partial_update(response):
        get_json = response.json()
        get_firstname = get_json["firstname"]
        get_lastname = get_json["lastname"]
        check_json = {
            "firstname": get_firstname,
            "lastname": get_lastname
        }
        return check_json
    return function_check_partial_update
