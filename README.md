# Проект для автоматического тестирования API с помощью PyTest и Docker

Всем привет, это мой домашний проект по тестированию **API** с помощью **PyTest** и **Docker**, пока он в процессе 
разработки. Начать мне помог пройденный курс на **Stepik.ru** - *Тестирование ПО: Автоматизация и 
Программирование на 
Python. API* (сертификат можно просмотреть [тут](https://stepik.org/cert/2145502)). 

**Однако**, уже сейчас можно запустить и посмотреть на работу нескольких тестов. Для запуска нужно:
1. Установить **Python** не ниже версии **3.10**, далее установить зависимости проекта командой:
    ```sh
    pip3 install -r requirements.txt
    ```
1. Установить **Docker** и запустить тестовый **API** в контейнере командой из корня проекта:
    ```sh
    ./start.sh --start
    ```
   (за тестовое приложение спасибо *Mark Winteringham*, ссылка на [оригинальный проект](https://github.com/mwinteringham/restful-booker), локально документацию после запуска контейнера можно посмотреть [тут](http://localhost:3001/apidoc/index.html));


3. Запустить тесты из корня проекта командой:
    ```sh
    python -m pytest -sv
    ```

Так же доступно разделение на позитивные и негативные тесты, с помощью маркировки, например:
 * `python -m pytest -sv -m positive` - запуск только **позитивных** тестов;
 * `python -m pytest -sv -m negative` - запуск только **негативных** тестов.

# Доработки
В ближайшем будущем планирую:
1. Полностью покрыть тестами выбранный **API**;
2. Добавить отчёты в **Allure**;
3. А так же возможность запуска самих тестов в **Docker**-контейнере.
