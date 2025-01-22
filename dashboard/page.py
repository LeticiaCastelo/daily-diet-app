import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from dashboard.service import DashboardService


def show_dashboard():
    dashboard_service = DashboardService()
    meals = dashboard_service.get_meals()

    if meals:

        st.header("Dashboard")
        meals_df = pd.json_normalize(meals)

        all_meals = len(meals_df)
        in_diet = meals_df['in_diet'].sum()
        off_diet = all_meals - in_diet

        col1, col2, col3 = st.columns(3)  
        col1.metric('Total de refeições registradas', all_meals, border=True)
        col2.metric('Refeições dentro da dieta', in_diet, border=True)
        col3.metric('Refeições fora da dieta', off_diet, border=True)


        labels = 'Refeições dentro da dieta', 'Refeições fora da dieta'
        sizes = [in_diet, off_diet]
        fig1, ax = plt.subplots(figsize=(3, 3))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
        textprops={'fontsize': 8}, labeldistance=1.1)
        ax.axis('equal')
        
        st.pyplot(fig1)

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
        
        fig2, ax = plt.subplots(figsize=(3,3))
        ax.pie(top_meals.values, labels=top_meals.index,  autopct='%1.1f%%', startangle=90,
        textprops={'fontsize': 8}, labeldistance=1.1)
        st.pyplot(fig2)

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

        fig3, ax = plt.subplots(figsize=(3,3))
        ax.pie(meals_type.values, labels=meals_type.index,  autopct='%1.1f%%', startangle=90,
        textprops={'fontsize':6}, labeldistance=1.1)
        st.pyplot(fig3) 

    else:
        st.warning('Nenhuma refeição foi encontrada.')