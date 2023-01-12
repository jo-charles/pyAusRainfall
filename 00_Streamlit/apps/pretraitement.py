import streamlit as st
import pandas as pd

DATASET_FOLDER = '../data/'

def app():
    st.title("Prétraitement des données")
    st.header("Titre")
    st.subheader("Variables du jeu de données")  
    st.write("""
    - Date : Date d'observation.
    - Location : Ville où se situe la station météorologique.
    - MinTemp : Température minimale en degrés Celsius.
    - MaxTemp : Température maximale en degrés Celsius.
    - Rainfall : Quantité de pluie enregistrée pour la journée en millimètres.
    - Evaporation : Niveau des bacs d'évaporation de classe A (en mm) dans les 24 heures jusqu'à 9h.
    - Sunshine : Nombre d'heures d'ensoleillement dans la journée.
    - WindGustDir : Direction des plus fortes rafales de vent dans les 24 heures jusqu'à minuit.
    - WindGustSpeed : Vitesse en km/h des plus fortes rafales de vent dans les 24 heures jusqu'à minuit.
    - WindDir9am : Direction du vent à 9h du matin.
    - WindDir3pm : Direction du vent à 3h de l'après-midi.
    - WindSpeed9am : Vitesse du vent en km/h moyennée sur 10 minutes avant 9h du matin.
    - WindSpeed3pm : Vitesse du vent en km/h moyennée sur 10 minutes avant 3h de l'après-midi.
    - Humidity9am : Humidité en pourcentage à 9h du matin.
    - Humidity3pm : Humidité en pourcentage à 3h de l'après-midi.
    - Pressure9am : Pression atmosphérique (hpa) au niveau de la mer à 9h.
    - Pressure3pm : Pression atmosphérique (hpa) au niveau de la mer à 15h.
    - Cloud9am : Opacité du ciel obscurci par les nuages à 9h mesuré en "oktas (0 signifie que le ciel est complètement éclairci tandis que 8 indique que le ciel est couvert.
    - Cloud3pm : Opacité du ciel obscurci par les nuages à 15h mesuré en "oktas
    - Temp9am : Température en degrés Celsius à 9h du matin.
    - Temp3pm : Température en degrés Celsius à 3h de l'après-midi.
    - RainToday : vaut 1 si les précipitations (en mm) dans les 24 heures avant 9h sont supérieur à 1 mm, 0 sinon.
    - RainTomorrow : vaut 1 si les précipitations (en mm) du lendemain sont supérieur à 1 mm, 0 sinon
    """)              
             
    st.warning("""
    Dans un premier temps, nous avons supprimé les valeurs manquantes des variables RainTomorrow et RainToday. Nous avons ensuite encodé ses variables pour que la valeur “Non” soit remplacée par 0 et la valeur “Oui” soit remplacée par 1.
Nous avons utilisé la méthode KNN-Imputer() pour les variables numériques présentant la plus forte proportion de valeurs manquantes (Sunshine, Evaporation, Cloud3pm, Cloud9am). Concernant les variables quantitatives restantes, l’utilisation de l’interpolation avec la méthode ‘time’, nous a permis de remplacer les valeurs manquantes. Pour finir, les valeurs manquantes des trois variables qualitatives WindGustDir, WindDir9am, WindDir3pm ont été respectivement remplacées par le mode.
Deux variables ont été créées; Temp_Delta_MinMax qui est la différence entre MaxTemp et MinTemp et Humidity_Delta qui est la différence entre les variables d’humidité.
""")

