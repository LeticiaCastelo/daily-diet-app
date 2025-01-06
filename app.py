import streamlit as st
import requests
from meals.meals_list import meals

API_URL = "http://127.0.0.1:5000"

def main():
    st.title("Daily Diet API - Statistics")

    menu_options = st.sidebar.selectbox(
        'Selecione uma opção', 
        ['Refeições Registradas']
    )

    if menu_options == "Refeições Registradas":
        meals()


if __name__ == '__main__':
    main()