import allure
import pytest
from tests.config.configuration import health_check_url, auth_token_url
from utils.http_methods import HttpMethods


@allure.epic("Секция проверки аутентификации и health-сheck")
class TestAuthAndHealthCheck:

    @allure.description("Проверка health-сheck")
    @pytest.mark.positive
    def test_get_Health_Check_expected_201(self):
        response = HttpMethods.get(health_check_url)
        assert response.status_code == 201, f'Статус-код некорректен, фактическое значение:\n {response.status_code}'
        assert response.text == 'Created', f'Фактический ответ не соответствует ожидаемому, фактический:\n {response.text}'

    @allure.description("Проверка аутентификации")
    @pytest.mark.positive
    def test_post_Create_Auth_Token_expected_201(self, auth_data, check_json_key_value):
        response = HttpMethods.post(auth_token_url, body=auth_data["body_for_create_auth_token"])
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение:\n {response.status_code}'
        check_json_key_value(response, 'token', 'unknown value', check_non_empty=True)

    @allure.description("Проверка аутентификации с неверными логином/паролем")
    @pytest.mark.negative
    def test_post_Create_Auth_Token_with_Bad_Credentials_expected_200(self, auth_data):
        response = HttpMethods.post(auth_token_url, body=auth_data["body_for_create_auth_token_with_bad_credentials"])
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        assert response.json() == auth_data[
            'expected_response_create_auth_token_with_bad_credentials'],\
            f'Фактический ответ не соответствует ожидаемому, фактический:\n {response.status_code}'
