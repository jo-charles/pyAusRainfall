import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict
from selection import select
import joblib
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance

def app():
    st.title("Démonstration")
    st.header("Predictions avec le modele")
    st.subheader("Interpretabilité du modèle")
    st.markdown(
            """
            A comparitive study of the performance of the various modeles led to the selection of Random Forest as the model of choice for this project. However, there are times when a performant model will not be the best choice if its interpretability is not sufficient for the end goal. With this in mind, the feature importance was studied. Voici les résultats du modèle par l'importance des variables en considérant la diminution moyenne de l'impureté pour tous les arbres de notre forêt.
            Une étude comparative des performances des différents modèles a mené à la sélection de la forêt aléatoire comme modèle de choix pour ce projet. Cependant, le modèle le plus performant n'est pas toujours le meilleur choix si son interprétabilité n'est pas suffisante pour le but final. L'importance des différentes features a donc été étudiée avec ceci en tête. Voici l'importance des features sur les résultats du modèle, en considérant la diminution moyenne de l'impureté pour tous les arbres de notre forêt.
            """
    )
    cola, colb = st.columns([70,30])
    # import model
    df = pd.read_csv('../data/weatherAUS_preprocessed.csv', index_col=0)
    data = df.drop('RainTomorrow', axis=1)
    clf_rf = joblib.load("../04_Model_Interpretability/rf_model.sav")
    fig, ax = plt.subplots()
    feature_imp = pd.Series(clf_rf.feature_importances_, index=data.columns)
    feature_imp.nlargest(13).plot(kind='barh')
    ax.set_xlabel("Diminution Moyenne de l'Impureté (MDI)")
    ax.set_title("Importance des variables")
    cola.pyplot(fig)
    
    st.markdown(
        """
        We can use the results of the feature importance to demonstrate the predictive power of the model and to get an intuitive understanding of how we should interpret them. First we can select one data point at random from the entire data set, and focus in on the values for the most important features within. 
        Nous pouvons utiliser les resultats de l'importance des features pour démontrer le pouvoir de prédiction du modèle, et comprendre de manière plus intuitive comment les interprêter. D'abord, nous allons sélectionner une donnée au hasard parmi tout le data set, et se focaliser seulement sur les variables les plus importantes. """
    )
    
    
    # insert buttons for demonstration section
    choice = st.button(label="Choix au hasard", key = 'c')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    if "selected" not in st.session_state:
        st.session_state.selected=0
        
    if "scaled_features" not in st.session_state:
        st.session_state.scaled_features = 0
        
    if "actual_result" not in st.session_state:
        st.session_state.actual_result = 0
    
    if choice:
        selected, scaled_features, actual_result = select()
        print(f"{actual_result=}")
        st.session_state.selected = selected
        st.session_state.scaled_features = scaled_features
        st.session_state.actual_result = actual_result
        with col1:
            st.text('RainToday (mm)')
            st.text(selected['Rainfall'].iloc[0])
        with col2:
            st.text('Humidity (%)')
            st.text(selected['Humidity3pm'].iloc[0])
        with col3:
            st.text('Pressure (hpa)')
            st.text(selected['Pressure9am'].iloc[0])
        with col4:
            st.text('WindGustSpeed (km/h)')
            st.text(selected['WindGustSpeed'].iloc[0])
        with col5:
            st.text('Temp (C)')
            st.text(selected['Temp3pm'].iloc[0])

    
    st.markdown(
        
       """
       Next we use our model to make a prediction about whether we should plan to take our umbrella the following day.
       Ensuite, nous allons utiliser le modèle pour prédire s'il faut prévoir le parapluie le jour suivant. """
    )
    
    
    question = st.button(label="D'apres le modele: Pluie demain?", key='q')
    
    if question:
        result = predict(st.session_state.scaled_features)
        st.text(result)

    st.markdown(
        """
        Finally we check whether our prediction was correct or not by comparing it against the actual result.
        Enfin, nous allons vérifier si la prédiction était correcte, en révélant le résultat réel. 
        """
    )
    
    verite = st.button(label="Verité", key='v')
#    end = st.button(key="end", label='end')
    
    if verite:
        st.text(bool(st.session_state.actual_result.iloc[0]))

        
    st.markdown(
        """
        Repetition of ths process allows the user themselves to notice that, for example, a higher humidity is reflected in a higher chance of rain the following day.
        La répétition de ce processus permet à l'utilisateur de remarquer soi-même que, par exemple, un taux d'humidité plus élevé indique un risque de pluie plus élevé le lendemain.
        """
    )
#    if end:
#        pass
    #end while
