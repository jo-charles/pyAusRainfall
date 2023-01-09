import streamlit as st
import pandas as pd

DATASET_FOLDER = '../data/'

def app():
    st.title("Analyse exploratoire des données")
    st.warning("""Dans un premier temps, nous avons supprimé les valeurs manquantes des variables RainTomorrow et RainToday. Nous avons ensuite encodé ses variables pour que la valeur “Non” soit remplacée par 0 et la valeur “Oui” soit remplacée par 1.
Nous avons utilisé la méthode KNN-Imputer() pour les variables numériques présentant la plus forte proportion de valeurs manquantes (Sunshine, Evaporation, Cloud3pm, Cloud9am). Concernant les variables quantitatives restantes, l’utilisation de l’interpolation avec la méthode ‘time’, nous a permis de remplacer les valeurs manquantes. Pour finir, les valeurs manquantes des trois variables qualitatives WindGustDir, WindDir9am, WindDir3pm ont été respectivement remplacées par le mode.
Deux variables ont été créées; Temp_Delta_MinMax qui est la différence entre MaxTemp et MinTemp et Humidity_Delta qui est la différence entre les variables d’humidité.
""")
    st.header("Quelles variables vous semblent les plus pertinentes au regard de vos objectifs ?")  
    st.write("\n\n")
    st.write("""Les variables qui nous semblent les plus pertinentes afin de prédire la pluie au lendemain sont : 
RainToday car en général un épisode de fortes pluies est rarement isolé et s’accompagne donc de plusieurs autres épisodes dans le temps.
Humidity3pm et Humidity9am, en effet, un taux d’humidité important au jour J peut indiquer que nous traversons plusieurs périodes pluvieuses.""")
    data_load_state = st.text('Loading data...')
    data = pd.read_csv(DATASET_FOLDER + "weatherAUS.csv")
    data_load_state.text("")
    st.dataframe(data.head(10))
    if st.checkbox("Afficher le résumé "):
        st.write(data.describe())
