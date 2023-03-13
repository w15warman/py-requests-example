import logging
from jsonschema import validate
from register.requests import ApiClient

logger = logging.getLogger("api")


class User:
    def __init__(self, url):
        self.url = url
        self.api_client = ApiClient()

    POST_USER = '/user'

    def create_user(self, body: dict, schema: dict):
        response = self.api_client.send_request("POST", f"{self.url}{self.POST_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return response

    def get_user_by_name(self, username: str):
        response = self.api_client.send_request("GET", f"{self.url}{self.POST_USER}/{username}")
        logger.info(response.text)
        return response

    def update_user(self, body: dict, username: str):
        response = self.api_client.send_request("PUT", f"{self.url}{self.POST_USER}/{username}", json=body)
        logger.info(response.text)
        return response

    def delete_user(self, username: str):
        response = self.api_client.send_request("DELETE", f"{self.url}{self.POST_USER}/{username}")
        logger.info(response.text)
        return response

    GET_USER_LOGIN = '/user/login'

    def login_user(self, params: dict):
        response = self.api_client.send_request("GET", f"{self.url}{self.GET_USER_LOGIN}", params=params)
        logger.info(response.text)
        return response
