import pytest
import json


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
