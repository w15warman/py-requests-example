from faker import Faker

from register.user_api import User
from register.models import CreateUser
from schemas.user_creation import valid_schema

fake = Faker()
URL = "https://petstore.swagger.io/v2"
username = "w16"


class TestRegistration:
    def test_user_creation(self):
        request_body = CreateUser.random(username)
        response = User(url=URL).create_user(body=request_body, schema=valid_schema)
        assert response.status_code == 200
        assert response.json().get("message") is not None

    def test_get_user_by_username(self):
        response = User(url=URL).get_user_by_name(username)
        assert response.status_code == 200

    def test_update_user(self):
        new_name = fake.first_name_male()
        body = CreateUser.random(new_name)
        response = User(url=URL).update_user(body=body, username=username)
        assert response.status_code == 200

    def test_delete_user(self):
        response = User(url=URL).delete_user(username)
        assert response.status_code == 200

    def test_delete_user_not_exist(self):
        response = User(url=URL).delete_user(username='ajgdkag433##sjkgdaskg')
        assert response.status_code == 404

    def test_login_invalid_creds(self):
        path_params = {'username': 'fdhskjfds', 'password': '32748239'}
        response = User(url=URL).login_user(params=path_params)
        assert response.status_code == 200
