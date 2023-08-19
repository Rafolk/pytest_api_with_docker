from tests.config.configuration import health_check_url, auth_token_url
from utils.http_methods import HttpMethods



class TestAuthAndHealthCheck:

    def test_get_Health_Check_expected_201(self):
        response = HttpMethods.get(health_check_url)
        assert response.status_code == 201, f'The status code is incorrect, the actual value = {response.status_code}'
        assert response.text == 'Created', f'The response text is incorrect, the actual value = {response.text}'

    def test_post_Create_Auth_Token_expected_201(self, auth_data, check_json_key_value):
        response = HttpMethods.post(auth_token_url, body=auth_data["body_create_auth_token"])
        assert response.status_code == 200, f'The status code is incorrect, the actual value =  {response.status_code}'
        check_json_key_value(response, 'token', 'unknown value', check_non_empty=True)
