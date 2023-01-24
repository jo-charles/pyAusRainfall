import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

DATASET_FOLDER = '../data/'

def app():
    st.title("Visualisation des données")
    st.header("Distribution de la variable RainTomorrow et RainToday") 
    data = pd.read_csv(DATASET_FOLDER + "weatherAUS.csv")
    # distribution de la variable 'RainToday'
    fig = plt.figure(figsize=(14,6))
    ax1 = plt.subplot(1, 2, 1)
    ax1 = sns.countplot(x='RainToday', data=data)
    ax1 = plt.title("Distribution de la variable 'RainToday'", fontsize=12)
    ax1 = plt.xlabel("'RainToday'")
    ax1 = plt.ylabel("Nombre d'observations")

    # distribution de la variable cible 'RainTomorrow'
    ax2 = plt.subplot(1, 2, 2)
    ax2 = sns.countplot(x='RainTomorrow', data=data)
    ax2 = plt.title("Distribution de la variable cible 'RainTomorrow'", fontsize=12)
    ax2 = plt.xlabel("'RainTomorrow'")
    ax2 = plt.ylabel("Nombre d'observations") 
    st.pyplot(fig)
    st.write("""
    Les variables RainToday et RainTomorrow présentent une forte disparité entre leurs classes, avec :
22.4% des observations qui correspondent à la classe minoritaire "Yes",
77.6% des observations qui correspondent à la classe majoritaire "No".
Il s'agit d'un problème de classification binaire sur jeu de données déséquilibré.
""")
    st.header("Etude statistique descriptive des variables qualitatives") 
    cat_features = [col for col in data.columns if data[col].dtype == 'O']
    cat_data = data.select_dtypes(include = 'O')
    st.write(cat_data.describe())
    st.write("""
    La variable "Date" présente un nombre très élevé de modalités qui ne recouvre pas entièrement une période de 10 ans. Certains jours manquent donc de données. Il est absolument nécessaire de modifier cette variable pour réduire sa cardinalité.
Les variables "Location", "WindGustDir", "WindDir9am" et "WindDir3pm" présentent un nombre important de modalités.
Les variables "RainToday" et "RainTomorrow" ne contiennent que deux modalités qui seront encodées en données binaires.
Les variable qualitatives présentant une forte cardinalité posent problème car la taille de la matrice de données augmente significativement lorsque ces variable sont encodées. Concernant la variable "Location", il est ainsi possible soit de l'ignorer, soit de regrouper les villes par différents secteurs de l'Australie et ainsi réduire son nombre de classes distinctes.
""")

    st.header("Etude statistique descriptive des variables quantitatives") 
    st.write(data.describe())
    st.header("Sélection de variables") 
    st.header("Distribution de la variable de précipitations (Rainfall)") 
    data2 = pd.read_csv(DATASET_FOLDER + "weatherAUS_preprocessed.csv")
    fig1 = plt.figure(figsize=(8,8))
    sns.kdeplot(data2['Rainfall'], shade='True')
    plt.title("Distribution de la variable 'Rainfall'", fontsize=10);
    st.pyplot(fig1)
    st.write("""
    La distribution de la variable "Rainfall" est fortement concentrée autour des valeurs 0 mm et 2 mm.
""")
    data['year'] = pd.to_datetime(data['Date']).dt.year
    fig2 = sns.catplot(x='year', y='Rainfall', kind='bar', height=8, hue='RainTomorrow', data=data)  
    st.pyplot(fig2)