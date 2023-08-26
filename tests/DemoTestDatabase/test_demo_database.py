import allure
import pytest


@allure.epic("Секция демо-тестов базы данных")
class TestDemoDatabase:

    # @pytest.mark.skip("Таблица уже была создана ранее.")
    @allure.description("Проверка создания таблицы.")
    @pytest.mark.positive
    def test_Create_Table(self, db_connection):
        db_connection.execute(
                """CREATE TABLE users(
                    id serial PRIMARY KEY,
                    first_name varchar(50) NOT NULL,
                    nick_name varchar(50) NOT NULL);"""
                )
        assert db_connection.statusmessage == "CREATE TABLE", f'Возникла ошибка при создании таблицы:\n' \
                                                              f' {db_connection.statusmessage}'

    # @pytest.mark.skip("В разработке.")
    @allure.description("Проверка созданной ранее таблицы.")
    @pytest.mark.positive
    def test_Check_Create_Table(self, db_connection):
        db_connection.execute(
            """SELECT column_name, data_type, character_maximum_length
                FROM information_schema.columns
                WHERE table_name = 'users';"""
            )
        expected_result = [('id', 'integer', None), ('first_name', 'character varying', 50), ('nick_name', 'character varying', 50)]
        assert db_connection.fetchall() == expected_result, f'Не прошла проверка ранее созданной таблицы.'
