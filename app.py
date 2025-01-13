import streamlit as st
from meals.page import show_meals

API_URL = "http://127.0.0.1:5000"

def main():
        st.title("Daily Diet App")

        menu_options = st.sidebar.selectbox(
            'Selecione uma opção', 
            ['Início','Refeições Registradas']
        )

        if menu_options ==  "Início":
            st.write('Tela de início')
        if menu_options == "Refeições Registradas":
            return show_meals()


if __name__ == '__main__':
    main()