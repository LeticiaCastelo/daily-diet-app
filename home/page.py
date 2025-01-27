import streamlit as st
import pandas as pd
from home.service import HomeService
import plotly.express as px

def show_home():
    home_service = HomeService()
    meals = home_service.get_meals()

    if meals:

        st.header("Estatísticas das Refeições")
        meals_df = pd.json_normalize(meals)

        all_meals = len(meals_df)
        in_diet = meals_df['in_diet'].sum()
        off_diet = all_meals - in_diet

        col1, col2, col3 = st.columns(3)  
        col1.metric('Total de refeições registradas', all_meals, border=True)
        col2.metric('Refeições dentro da dieta', in_diet, border=True)
        col3.metric('Refeições fora da dieta', off_diet, border=True)

        labels = ['Refeições dentro da dieta', 'Refeições fora da dieta']
        values = [in_diet, off_diet]

        fig1 = px.pie(
            names=labels, 
            values=values, 
            hole=0.3,  
        )
        
        st.plotly_chart(fig1)

        st.divider()
        
        st.subheader("Top 3 Refeições Mais Registradas")
        col1, col2, col3 = st.columns(3)  
        top_meals = meals_df['description'].value_counts().head(3)

        for i, (description, count) in enumerate(top_meals.items()):
            if i == 0:
                col1.metric(label=f"1º - {description}", value=count, border=True)
            if i == 1:
                col2.metric(label=f"2º - {description}", value=count, border=True)
            if i == 2:
                col3.metric(label=f"3º - {description}", value=count, border=True)
        
        labels = top_meals.index
        values = top_meals.values
        
        fig2 = px.pie(
            names=labels, 
            values=values, 
            hole=0.3,   
        )
        
        st.plotly_chart(fig2)

        st.divider()

        st.subheader("Distribuição de Refeições por Categoria")
        meals_type = meals_df['name'].value_counts()
        col1, col2, col3, col4 = st.columns(4) 
        for i, (name, count) in enumerate(meals_type.items()):
            if i == 0:
                col1.metric(label=name, value=count, border=True)
            if i == 1:
                col2.metric(label=name, value=count, border=True)
            if i == 2:
                col3.metric(label=name, value=count, border=True)
            if i == 3:
                col4.metric(label=name, value=count, border=True)

        labels = meals_type.index
        values = meals_type.values
        
        fig3 = px.pie(
            names=labels, 
            values=values, 
            hole=0.3,   
             
        )
        
        st.plotly_chart(fig3)

        
    else:
        st.warning('Nenhuma refeição foi encontrada.')