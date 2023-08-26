import psycopg2
import pytest
from tests.config.configuration import database_connection


# Фикстура для подключения к базе данных
@pytest.fixture(scope='session')
def db_connection():
    try:
        connect_db = psycopg2.connect(database_connection)
        connect_db.autocommit = True
        cursor = connect_db.cursor()
        yield cursor
        cursor.close()
        connect_db.close()
        print("\n[INFO] Подключение к БД закрыто.")

    except Exception as _ex:
        print("\n[INFO] Возникли ошибки при подключении к БД: ", _ex)
