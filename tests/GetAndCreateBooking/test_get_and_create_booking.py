import pytest
from tests.config.configuration import get_or_create_booking_url, get_current_booking_url
from utils.http_methods import HttpMethods


class TestGetAndCreateBooking:

    @pytest.mark.positive
    def test_get_Get_All_Booking_Ids_expected_200(self, check_booking_ids):
        response = HttpMethods.get(get_or_create_booking_url)
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        check_booking_ids(response)

    # Тут должны быть тесты с дополнительными параметрами запроса

    @pytest.mark.positive
    def test_get_Get_Current_Booking_expected_200(self, get_exist_booking_ids, check_json_key, check_type_data_key_value):
        link_for_get_current_booking = get_current_booking_url + str(get_exist_booking_ids)
        response = HttpMethods.get(link_for_get_current_booking)
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        check_type_data_key_value(response)

    @pytest.mark.positive
    def test_post_Create_New_Booking_expected_200(self, get_and_create_data):
        response = HttpMethods.post(get_or_create_booking_url, body=get_and_create_data["body_for_create_booking"])
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        response_json = response.json()
        assert get_and_create_data["body_for_create_booking"] == response_json.get("booking"), \
            f'Фактический ответ о бронировании не совпадает с ожидаемым, фактический:\n {response.text}'
        assert type(response_json["bookingid"]) == int, f'Тип данных значения ключа из ответа ошибочный.'

        link_for_check_post = get_current_booking_url + str(response_json.get("bookingid"))
        check_post = HttpMethods.get(link_for_check_post)
        assert get_and_create_data["body_for_create_booking"] == check_post.json(), \
            f'Get-запрос о свежесозданном бронировании содержит некорректную информацию, фактическимй ответ:\n ' \
            f'{response.text}'
