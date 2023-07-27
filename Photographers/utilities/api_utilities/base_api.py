import requests


class BaseAPI:
    def __init__(self, token, env):
        self.__base_url = env.base_api
        self.__headers = {'Accept': '*/*', 'Content-Type': 'application/json'}
        self.__request = requests

    def get(self, url, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def put(self, url, body, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.put(f'{self.__base_url}{url}', headers=headers, json=body)
        return response

    def post(self, url, body, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.post(f'{self.__base_url}{url}', json=body, headers=headers)
        return response

    def patch(self, url, body, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.patch(f'{self.__base_url}{url}', json=body, headers=headers)
        return response

    def delete(self, url, booking_id, headers=None):
        if headers is None:
            headers = self.__headers
        response = self.__request.get(f'{self.__base_url}{url}{booking_id}', headers=headers)
        return response
