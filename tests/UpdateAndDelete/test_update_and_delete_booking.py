import pytest
from tests.config.configuration import get_or_update_and_delete_booking_url
from utils.http_methods import HttpMethods


class TestGetAndCreateBooking:

    # @pytest.mark.skip(reason="не доделан")
    @pytest.mark.positive
    def test_put_Update_Booking_expected_200(self, update_and_delete_data, get_exist_booking_ids, auth_token_in_cookie):
        link_for_update_current_booking = get_or_update_and_delete_booking_url + str(get_exist_booking_ids)
        response = HttpMethods.put(link_for_update_current_booking, body=update_and_delete_data[
            "body_for_update_booking"], cookies=auth_token_in_cookie)
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'

        # Проверка обновления бронирования get-запросом
        check_put = HttpMethods.get(link_for_update_current_booking)
        assert update_and_delete_data["body_for_update_booking"] == check_put.json(), \
            f'Get-запрос о свежесозданном бронировании содержит некорректную информацию, фактическимй ответ:\n ' \
            f'{response.text}'
