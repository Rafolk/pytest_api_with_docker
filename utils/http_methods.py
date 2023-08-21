import allure
import requests


# Список кастомных http-методов
class HttpMethods:
    default_headers = {'Content-Type': 'application/json'}
    default_cookies = ""


    @staticmethod
    def get(url, headers=None, cookies=None):
        with allure.step("GET"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.get(url, headers=headers, cookies=cookies)
            return result

    @staticmethod
    def post(url, body, headers=None, cookies=None):
        with allure.step("POST"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.post(url, json=body, headers=headers, cookies=cookies)
            return result

    @staticmethod
    def put(url, body, headers=None, cookies=None):
        with allure.step("PUT"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.put(url, json=body, headers=headers, cookies=cookies)
            return result

    @staticmethod
    def patch(url, body, headers=None, cookies=None):
        with allure.step("PATCH"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.patch(url, json=body, headers=headers, cookies=cookies)
            return result

    @staticmethod
    def delete(url, body=None, headers=None, cookies=None):
        with allure.step("DELETE"):
            headers = headers or HttpMethods.default_headers
            cookies = cookies or HttpMethods.default_cookies
            result = requests.delete(url, json=body, headers=headers, cookies=cookies)
            return result
