import requests

class Auth:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:5000'
        self.__auth_url = f'{self.__base_url}/login'

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password
        }
        auth_response = requests.post(
            self.__auth_url,
            json=auth_payload
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao autenticar. Status code: {auth_response.status_code}'}