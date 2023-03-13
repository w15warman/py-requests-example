import requests
from requests import Response


class ApiClient:
    @staticmethod
    def send_request(method: str, url: str, **kwargs) -> Response:
        """
        :param method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        :param url: URL for the new Request object.
        :param kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        :return:
        """
        return requests.request(method, url, **kwargs)
