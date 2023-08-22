import allure
import pytest
from tests.config.configuration import get_or_update_and_delete_booking_url
from utils.http_methods import HttpMethods


@allure.epic("Секция проверки обновления и удаления бронирования")
class TestUpdateAndDeleteBooking:

    @allure.description("Проверка полного обновления бронирования")
    @pytest.mark.positive
    def test_put_Update_Booking_expected_200(self, update_and_delete_data, get_exist_booking_ids, auth_token_in_cookie):
        link_for_update_current_booking = get_or_update_and_delete_booking_url + str(get_exist_booking_ids(0))
        response = HttpMethods.put(link_for_update_current_booking, body=update_and_delete_data[
            "body_for_update_booking"], cookies=auth_token_in_cookie)
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'

        # Проверка обновления бронирования get-запросом
        check_put = HttpMethods.get(link_for_update_current_booking)
        assert update_and_delete_data["body_for_update_booking"] == check_put.json(), \
            f'Get-запрос о свежесозданном бронировании содержит некорректную информацию, фактический ответ:\n ' \
            f'{response.text}'

    @allure.description("Проверка частичного обновления бронирования")
    @pytest.mark.positive
    def test_patch_Partial_Update_Booking_expected_200(self, update_and_delete_data, get_exist_booking_ids,
                                              auth_token_in_cookie, check_partial_update):
        link_for_update_partial_booking = get_or_update_and_delete_booking_url + str(get_exist_booking_ids(1))
        response = HttpMethods.patch(link_for_update_partial_booking, body=update_and_delete_data[
            "body_for_partial_update_booking"], cookies=auth_token_in_cookie)
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'

        # Проверка частичного обновления бронирования get-запросом
        check_put = HttpMethods.get(link_for_update_partial_booking)
        check_json = check_partial_update(check_put)
        assert update_and_delete_data["body_for_partial_update_booking"] == check_json, \
            f'Get-запрос о свежесозданном бронировании содержит некорректную информацию, фактический ответ:\n ' \
            f'{response.text}'

    @allure.description("Проверка удаления бронирования")
    @pytest.mark.positive
    def test_Delete_Booking_expected_201(self, get_exist_booking_ids, auth_token_in_cookie):
        link_for_delete_booking = get_or_update_and_delete_booking_url + str(get_exist_booking_ids(5))
        response = HttpMethods.delete(link_for_delete_booking, cookies=auth_token_in_cookie)
        assert response.status_code == 201, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        assert response.text == 'Created'

        # Проверка удаления бронирования get-запросом
        check_delete = HttpMethods.get(link_for_delete_booking)
        assert check_delete.status_code == 404, f'Статус-код проверки удаления некорректен, фактическое значение =' \
                                                f' {response.status_code}'
        assert check_delete.text == 'Not Found', \
            f'Get-запрос с удалённым бронированием содержит некорректную информацию, фактический ответ:\n ' \
            f'{response.text}'
