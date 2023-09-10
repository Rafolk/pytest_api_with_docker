import allure
import requests


# Список кастомных http-методов
class HttpMethods:
    default_headers = {'Content-Type': 'application/json'}
    default_cookies = ""


    @staticmethod
    def get(url, headers=None, cookies=None):
        with allure.step(f"GET-запрос по адресу : '{url}'"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.get(url, headers=headers, cookies=cookies)
        with allure.step(f"В качестве ответа на GET-запрос получено : '\n{result.text}'"):
            return result

    @staticmethod
    def post(url, body, headers=None, cookies=None):
        with allure.step(f"POST-запрос по адресу : '{url}' , с телом : '\n{body}'"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.post(url, json=body, headers=headers, cookies=cookies)
        with allure.step(f"В качестве ответа на POST-запрос получено : '\n{result.text}'"):
            return result

    @staticmethod
    def put(url, body, headers=None, cookies=None):
        with allure.step(f"PUT-запрос по адресу : '{url}' , с телом : '\n{body}'"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.put(url, json=body, headers=headers, cookies=cookies)
        with allure.step(f"В качестве ответа на PUT-запрос получено : '\n{result.text}'"):
            return result

    @staticmethod
    def patch(url, body, headers=None, cookies=None):
        with allure.step(f"PATCH-запрос по адресу : '{url}' , с телом : '\n{body}'"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.patch(url, json=body, headers=headers, cookies=cookies)
        with allure.step(f"В качестве ответа на PATCH-запрос получено : '\n{result.text}'"):
            return result

    @staticmethod
    def delete(url, body=None, headers=None, cookies=None):
        with allure.step(f"DELETE-запрос по адресу : '{url}'"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.delete(url, json=body, headers=headers, cookies=cookies)
        with allure.step(f"В качестве ответа на DELETE-запрос получено : '\n{result.text}'"):
            return result
