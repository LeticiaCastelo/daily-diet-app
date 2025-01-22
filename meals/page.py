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
            key='meals_grid', 
            )
    else:
        st.warning('Nenhuma refeição encontrada')


    st.header('Registrar nova Refeição')

    name = st.selectbox('Nome da Refeição', ['Café da Manhã', 'Almoço', 'Lanche', 'Jantar'])
    description= st.text_input('Descrição da Refeição'),
    date = st.date_input('Data da Refeição')
    time= st.time_input('Horário da Refeição')
    in_diet= st.checkbox('Está na dieta?')

    description_str = description if isinstance(description, str) else str(description[0]).strip()
    date_str = date.strftime("%d-%m-%Y")
    time_str = time.strftime("%H:%M:%S")

    if st.button('Registrar'):
        new_meal = meals_service.create_meal(
            name=name,
            description=description_str,
            date=date_str,
            time=time_str,
            in_diet=in_diet
        )
        if new_meal:
            st.rerun()
        else:
            st.error("Erro ao registrar a refeição. Verifique os campos.")