import allure
import pytest
from tests.config.configuration import get_all_ids_or_create_booking_url, get_or_update_and_delete_booking_url
from utils.http_methods import HttpMethods


@allure.epic("Секция проверки получения информации о бронировании и его создания")
class TestGetAndCreateBooking:

    @allure.description("Проверка получения Id всех доступных бронирований")
    @pytest.mark.positive
    def test_Get_All_Booking_Ids_expected_200(self, check_booking_ids):
        response = HttpMethods.get(get_all_ids_or_create_booking_url)
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        check_booking_ids(response)

    @allure.description("Проверка запроса с фильтром по имени методом чёрного ящика")
    @pytest.mark.positive
    def test_Get_filter_name_Booking_expected_200(self, get_parametrize_value):
        response = HttpMethods.get(get_all_ids_or_create_booking_url + f'?firstname={get_parametrize_value["firstname"]}&lastname={get_parametrize_value["lastname"]}')
        assert response.status_code == 200, f'Статус-код запроса с фильтром некорректен, фактическое значение = {response.status_code}'

        # Проверка полученных Id на соответствие фильтру (в цикле, на случай нескольких совпадений по фильтру)
        response_json = response.json()
        for item in response_json:
            booking_id = item["bookingid"]
            check_response = HttpMethods.get(get_or_update_and_delete_booking_url + str(booking_id))
            assert check_response.status_code == 200, f'Статус-код проверки запроса с фильтром некорректен, фактическое значение = {response.status_code}'
            check_json = check_response.json()
            assert get_parametrize_value["firstname"] == check_json.get("firstname"), f'Фактический firstname не ' \
                                                                                   f'соответствует ожидаемому, фактическое значение = {get_parametrize_value["firstname"]}'
            assert get_parametrize_value["lastname"] == check_json.get("lastname"), f'Фактический lastname не ' \
                                                                                 f'соответствует ожидаемому, фактическое значение = {get_parametrize_value["lastname"]}'

    @allure.description("Проверка запроса с фильтром по дате въезда и выезда методом чёрного ящика")
    @pytest.mark.positive
    def test_Get_filter_booking_dates_Booking_expected_200(self, get_parametrize_value):
        response = HttpMethods.get(get_all_ids_or_create_booking_url + f'?checkin={get_parametrize_value["checkin"]}&checkout={get_parametrize_value["checkout"]}')
        assert response.status_code == 200, f'Статус-код запроса с фильтром некорректен, фактическое значение =' \
                                            f' {response.status_code}'

        # Проверка полученных Id на соответствие фильтру (в цикле, на случай нескольких совпадений по фильтру)
        response_json = response.json()
        for item in response_json:
            booking_id = item["bookingid"]
            check_response = HttpMethods.get(get_or_update_and_delete_booking_url + str(booking_id))
            assert check_response.status_code == 200, f'Статус-код проверки запроса с фильтром некорректен, фактическое значение = {response.status_code}'
            check_json = check_response.json()
            bookingdates = check_json.get("bookingdates")
            assert get_parametrize_value["checkin"] == bookingdates.get("checkin"), f'Фактический checkin не соответствует ожидаемому, ' \
                                                        f'фактическое значение = {get_parametrize_value["checkin"]}'
            assert get_parametrize_value["checkout"] == bookingdates.get("checkout"), f'Фактический checkout не ' \
                                                                                   f'соответствует ожидаемому, фактическое значение = {get_parametrize_value["checkout"]}'

    @allure.description("Проверка получения информации о конкретном бронировании по Id")
    @pytest.mark.positive
    def test_Get_Current_Booking_expected_200(self, get_exist_booking_ids, check_json_key, check_type_data_key_value):
        link_for_get_current_booking = get_or_update_and_delete_booking_url + str(get_exist_booking_ids(0))
        response = HttpMethods.get(link_for_get_current_booking)
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        check_type_data_key_value(response)

    @allure.description("Проверка создания нового бронирования")
    @pytest.mark.positive
    def test_post_Create_New_Booking_expected_200(self, get_and_create_data):
        response = HttpMethods.post(get_all_ids_or_create_booking_url, body=get_and_create_data["body_for_create_booking"])
        assert response.status_code == 200, f'Статус-код некорректен, фактическое значение = {response.status_code}'
        response_json = response.json()
        assert get_and_create_data["body_for_create_booking"] == response_json.get("booking"), \
            f'Фактический ответ о бронировании не совпадает с ожидаемым, фактический:\n {response.text}'
        assert type(response_json["bookingid"]) == int, f'Тип данных значения ключа из ответа ошибочный.'

        # Проверка создания нового бронирования get-запросом
        link_for_check_post = get_or_update_and_delete_booking_url + str(response_json.get("bookingid"))
        check_post = HttpMethods.get(link_for_check_post)
        assert get_and_create_data["body_for_create_booking"] == check_post.json(), \
            f'Get-запрос о свежесозданном бронировании содержит некорректную информацию, фактический ответ:\n ' \
            f'{response.text}'
