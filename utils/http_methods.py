import requests


# Список кастомных http-методов
class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookies = ""

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

    @staticmethod
    def post(url, body, headers=None):
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        return result
