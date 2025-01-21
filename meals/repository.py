import requests
import streamlit as st
from login.service import logout

class MealsRepository:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:5000'
        self.__meals_url = f'{self.__base_url}/user/meals'
        self.__new_meal_url = f'{self.__base_url}/user/new-meal'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_meals(self):
        response = requests.get(
            self.__meals_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')
    
    def create_meal(self, meal):
        response = requests.post(
            self.__new_meal_url,
            headers=self.__headers,
            json=meal
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code: {response.status_code}')
    