from .errors import InvalidCredentialsError, AuthenticationError, ServerError
from .utils import validate_base_url, validate_username


class Auth:
    __slots__ = ['__username', '__password', 'base_url', '__token']

    def __init__(self, username: str, password: str, base_url: str):
        validate_username(username=username)
        self.__username = username

        if type(password) is not str:
            raise InvalidCredentialsError('password can only be of type String')
        if password == '':
            raise InvalidCredentialsError('password cannot empty')
        self.__password = password

        validate_base_url(base_url=base_url)
        self.base_url = 'https://' + base_url

        self.__token = None

    def __fetch_token(self):
        from requests import post
        from json import dumps

        response = post(
            f"{self.base_url}/authservice/api/v1/auth/cli",
            headers={'Content-Type': 'application/json'},
            data=dumps({'email': self.__username, 'password': self.__password})
        )
        if response.status_code == 200:
            self.__token = "Bearer " + response.json()['data']
        elif response.status_code == 401:
            raise AuthenticationError(response.json()['message'])
        else:
            raise ServerError(f"Status code = {response.status_code}")

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_token(self) -> str:
        if self.__token is None:
            self.__fetch_token()
        return self.__token
