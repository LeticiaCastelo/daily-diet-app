import streamlit as st
from meals.page import show_meals
from dashboard.page import show_dashboard


API_URL = "http://127.0.0.1:5000"

def main():
        st.title("Daily Diet App")

        menu_options = st.sidebar.selectbox(
            'Selecione uma opção', 
            ['Página Inicial','Dashboard','Refeições Registradas']
        )

        if menu_options ==  "Página Inicial":
            st.write('Tela de início')
        if menu_options == "Refeições Registradas":
            return show_meals()
        if menu_options == "Dashboard":
            return show_dashboard()

if __name__ == '__main__':
    main()