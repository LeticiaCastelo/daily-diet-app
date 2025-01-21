import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from meals.service import MealsService

def show_meals():
    meals_service = MealsService()
    meals = meals_service.get_meals()

    
    if meals:
        st.header("Refeições Registradas")
        meals_df = pd.json_normalize(meals)
        AgGrid(
            data = pd.DataFrame(meals_df),
            reload_data=True,
            key='meals_grid', 
            )
    else:
        st.warning('Nenhuma refeição encontrada')


    st.title('Cadastrar nova Refeição')
    name = st.text_input('Nome da Refeição')
    if st.button('Cadastrar'):
        st.success(f'Refeição "{name}" cadastrada com sucesso.')