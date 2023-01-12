import streamlit as st
import pandas as pd

DATASET_FOLDER = '../data/'

def app():
    st.title("Visualisation des données")
    st.header("Titre")  
    st.write("""
    Les variables qui nous semblent les plus pertinentes afin de prédire la pluie au lendemain sont : 
RainToday car en général un épisode de fortes pluies est rarement isolé et s’accompagne donc de plusieurs autres épisodes dans le temps.
Humidity3pm et Humidity9am, en effet, un taux d’humidité important au jour J peut indiquer que nous traversons plusieurs périodes pluvieuses.
""")
    data_load_state = st.text('Loading data...')
    data = pd.read_csv(DATASET_FOLDER + "weatherAUS.csv")
    data_load_state.text("")
    st.dataframe(data.head(10))
    if st.checkbox("Afficher le résumé "):
        st.write(data.describe())

        