import pytest
from tests.config.configuration import get_all_booking_ids_url, get_current_booking_url
from utils.http_methods import HttpMethods


class TestGetAndCreateBooking:

    @pytest.mark.positive
    def test_get_Get_All_Booking_Ids_expected_200(self, check_booking_ids):
        response = HttpMethods.get(get_all_booking_ids_url)
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        check_booking_ids(response)

    # Тут должны быть тесты с дополнительными параметрами ссылки

    @pytest.mark.positive
    def test_get_Get_Current_Booking_expected_200(self, get_exist_booking_ids, check_json_key, check_type_data_key_value):
        link = get_current_booking_url + str(get_exist_booking_ids)
        response = HttpMethods.get(link)
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        check_type_data_key_value(response)
