import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

meals = [
    {
        "date": "24-12-2024",
        "time": "08:10",
        "name" : "Café da manhã",
        "description": "Café preto sem açúcar",
        "in_diet": True
        
    },
    {
        "date": "24-12-2024",
        "time": "12:10",
        "name": "Almoço",
        "description": "arroz, feijão, frango e salada",
        "in_diet": True
    },
    {
        "date": "30-12-2024",
        "time": "07:30",
        "name": "Café da manhã",
        "description": "4 torradas com geléia de morango",
        "in_diet": True
    },
    {
        "date": "30-12-2024",
        "time": "15:30",
        "name": "Lanche da tarde",
        "description": "Ovos cozidos",
        "in_diet": True
    },
    {
        "date": "30-12-2024",
        "time": "20:30",
        "name": "Jantar",
        "description": "2 fatias de pizza",
        "in_diet": False
    }
]
def show_meals():
    st.header("Refeições Registradas")
    AgGrid(
        data = pd.DataFrame(meals),
        key='meals_grid', 
        )
