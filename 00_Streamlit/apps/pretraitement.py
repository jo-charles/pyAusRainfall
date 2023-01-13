import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATASET_FOLDER = '../data/'

def app():
    st.title("Preprocessing")
    st.header("Variables du jeu de données")  
    st.markdown("""
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

    data_load_state = st.text('Loading data...')
    data = pd.read_csv(DATASET_FOLDER + "weatherAUS.csv")
    data_load_state.text("")
    
    if st.checkbox("Afficher le résumé "):
        st.dataframe(data.head(3))
        st.write(data.describe())
  
    st.header("Gestion des valeurs manquantes")

    st.markdown("""
             
    - 4 variables quantitatives possèdent environ 40% de valeurs manquantes (Sunshine, Evaporation, Cloud3pm, Cloud9am).\n
    Pour gérer ces valeurs manquantes, Nous avons utilisé le module Impute de scikit-learn et en particulier le transformer KNNImputer.\n
    Cette fonctionnalité permet de nettoyer notre dataset des valeurs manquantes qui le composes en remplaçant les valeurs manquantes d'un échantillon par les valeurs de ses plus proches voisin.
        
    - Les autres variables quantitatives possèdent moins de 10% de valeurs manquantes.\n
    S'agissant de de données temporelle, nous avons décidé d'interpoler les valeur manquante à l'aide de pandas'
    
    - Enfin nous avons remplacer les valeurs manquantes pour les variables qualitatives en utilisant le mode
    """)


    st.header("Ajout de variables")    

    st.markdown("""
             
    - Ajout d'une variable décrivant 4 types de climat en Australie ('chaud_humide', 'tempéré_froid', 'sec', 'méditerranéen')
    - Ajout de deux nouvelles variables qui nous semblaient pertinentes : “Temp_Delta_MinMax” et “Humidity_Delta”. 

    """)
    
    st.header("Gestion des variables catégorielles")
    
    st.markdown("""
             
    Afin d'alléger notre model, nous avons décidé de ne pas nous servir des variables catégorielles suivantes ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm']

    La seule variable catégorielle que nous avons gardé est la variable 'climat' qui est basée sur la variable Location.

    """)
    
    
    st.header("Corrélation de variables")
    
    df = pd.read_csv("../data/weatherAUS_Rev0.csv", index_col=0)
    # matrice de corrélation
    fig, ax = plt.subplots(figsize=(10,10))
    annot_kws={'fontsize':10, 'color':"k", 'verticalalignment':'center'}
    sns.heatmap(df.corr(), linewidths=0.5, annot=True, annot_kws=annot_kws, fmt=".2f", ax=ax, cmap='coolwarm', center=0)
    plt.title('Matrice de corrélation du jeu de données', fontsize="small")
    
    sns.set(rc={'figure.figsize':(10,10)})
    st.pyplot(fig)


    
    st.markdown("""
    - suppression des variables les moins corrélées à la variable cible (choix: 'inférieur à 0.15 en valeur absolue')
    - suppression de la date car ni l'année, le mois, la semaine ou la journée ne sont pas très corrélées
    - suppression de la variable "Humidity9am", moins corrélée à la variable cible que "Humidity_Delta"
    - suppression de la variable "Pressure3pm", moins corrélée à la variable cible que "Pressure9am"
    - suppression de la variable "Cloud9am", moins corrélée à la variable cible que "Cloud3pm"
    - suppression de la variable "MaxTemp", moins corrélée à la variable cible que "Temp3pm"
    """)
    
    st.header("Standardisation")
    st.markdown("""
    Nous avons standardisé nos données en utilisant la méthode standard car les features répondent à des distributions normales (Distributions Gaussiennes)
    """)    

    st.header("Résulats")   
    st.markdown("""    
    Finalement, après avoir écarté les variables catégorielles, remplacé certaines variables trop fortement corrélées entre elles et ajouté de nouvelles variables explicatives, le jeu de données a subi une réduction significative de 3.2% des observations et de 39,1% des variables.

    """)  