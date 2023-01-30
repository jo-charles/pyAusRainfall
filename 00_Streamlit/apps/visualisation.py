import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import chi2_contingency
from io import BytesIO

DATASET_FOLDER = '../data/'

def app():

    st.markdown("""<style>.normal-font {font-size:13.5pt}</style>""", unsafe_allow_html=True)
    st.title("Visualisation des données")
    st.header("Distribution des variables RainTomorrow et RainToday") 
    data = pd.read_csv(DATASET_FOLDER + "weatherAUS.csv")
   
    data_1 = data.drop(['Date'], axis=1, inplace = True)
    data_1 = data.drop_duplicates(inplace=True)
    
    data_under = pd.read_csv(DATASET_FOLDER + "weatherAUS_preprocessed.csv")

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

    buf = BytesIO()
    fig.savefig(buf, format="png")
    st.image(buf)

    table = pd.crosstab(data['RainToday'], data['RainTomorrow'])
    resultats_test = chi2_contingency(table)

    statistique = resultats_test[0]
    p_value = resultats_test[1]
    degre_liberte = resultats_test[2]

    if st.checkbox("*Résultat du test du chi2*"):
        st.write("""*statistique: 13799.479649324368,  p_value: 0.0*
""", unsafe_allow_html=True)
    #st.pyplot(fig)

    st.write("""
    Les variables RainToday et RainTomorrow présentent une forte disparité entre leurs classes, avec :
<p class="normal-font">- 22.4% des observations qui correspondent à la classe minoritaire "Yes",
<p class="normal-font">- 77.6% des observations qui correspondent à la classe majoritaire "No".
<p class="normal-font">Il s'agit d'un problème de classification binaire sur jeu de données déséquilibré.
""", unsafe_allow_html=True)

    st.header("Etude statistique descriptive des variables qualitatives") 
    cat_features = [col for col in data.columns if data[col].dtype == 'O']
    cat_data = data.select_dtypes(include = 'O')
    st.write(cat_data.describe())
    st.write("""
    <p class="normal-font">La variable "Date" présente un nombre très élevé de modalités qui ne recouvre pas entièrement une période de 10 ans. Certains jours manquent donc de données. Il est absolument nécessaire de modifier cette variable pour réduire sa cardinalité.
Les variables "Location", "WindGustDir", "WindDir9am" et "WindDir3pm" présentent un nombre important de modalités.
Les variables "RainToday" et "RainTomorrow" ne contiennent que deux modalités qui seront encodées en données binaires.
<p class="normal-font">Les variable qualitatives présentant une forte cardinalité posent problème car la taille de la matrice de données augmente significativement lorsque ces variable sont encodées. Concernant la variable "Location", il est ainsi possible soit de l'ignorer, soit de regrouper les villes par différents secteurs de l'Australie et ainsi réduire son nombre de classes distinctes.
""", unsafe_allow_html=True)

    st.header("Etude statistique descriptive des variables quantitatives") 
    st.write(data.describe())
 
    st.header("Visualisation des outliers") 
    st.write("""
    <p class="normal-font">En statistique,un outlier est une donnée aberrante ou une observation qui est « distante » des autres observations effectuées sur le même phénomène, c'est-à-dire qu'elle contraste grandement avec les valeurs « normalement » mesurées.
    """, unsafe_allow_html=True)
    fig2 = plt.figure(figsize = (4, 4))
    sns.boxplot(data = data[['Evaporation','Sunshine']]);
    plt.title("Boxplot des variables Evaporation et Sunshine", fontsize=12)
    buf = BytesIO()
    fig2.savefig(buf, format="png")
    st.image(buf)

    if st.checkbox("Afficher les outliers pour les variables de températures "):               
        fig3 = plt.figure(figsize = (10, 6))
        sns.boxplot(data = data[['MinTemp','MaxTemp','Temp9am','Temp3pm']]);
        buf = BytesIO()
        fig3.savefig(buf, format="png")
        st.image(buf)

    if st.checkbox("Afficher les outliers pour les variables du vents "):               
        fig4 = plt.figure(figsize = (5, 5))
        sns.boxplot(data = data[['WindGustSpeed','WindSpeed9am','WindSpeed3pm']]);
        buf = BytesIO()
        fig4.savefig(buf, format="png")
        st.image(buf)