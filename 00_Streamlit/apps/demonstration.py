import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict
from selection import select
from selection import scale_only
import joblib
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance

def app():
    st.title("Démonstration")
    st.header("Predictions avec le modele")
    st.subheader("Interpretabilité du modèle")
    st.markdown(
            """
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
        Nous pouvons utiliser les resultats de l'importance des features pour démontrer le pouvoir de prédiction du modèle, et comprendre de manière plus intuitive comment les interprêter. D'abord, nous allons sélectionner une donnée au hasard parmi tout le data set, et se focaliser seulement sur les variables les plus importantes. Ensuite, nous allons utiliser le modèle pour prédire s'il faut prévoir le parapluie le jour suivant, en precisant la confidence de cette prédiction. Enfin, nous allons vérifier si la prédiction était correcte, en révélant le résultat réel."""
    )
    
    
    # insert buttons for demonstration section
    choice = st.button(label="Choix au hasard", key = 'c')
    
    #col1, col2, col3, col4, col5 = st.columns(5)
    if "selected" not in st.session_state:
        st.session_state.selected=0
        
    if "scaled_features" not in st.session_state:
        st.session_state.scaled_features = 0
        
    if "actual_result" not in st.session_state:
        st.session_state.actual_result = 0
    
    if choice:
        col1, col2, col3, col4, col5 = st.columns(5)
        selected, scaled_features, actual_result = select()
        print(f"{actual_result=}")
        st.session_state.selected = selected
        st.session_state.scaled_features = scaled_features
        st.session_state.actual_result = actual_result
        with col3:
            st.write('Sunshine (h)')
            st.write(selected['Sunshine'].iloc[0])
        with col1:
            st.write('Humidity (%)')
            st.write(selected['Humidity3pm'].iloc[0])
        with col4:
            st.write('Pressure (hpa)')
            st.write(selected['Pressure9am'].iloc[0])
        with col5:
            st.write('WindGustSpeed (km/h)')
            st.write(selected['WindGustSpeed'].iloc[0])
        with col2:
            st.write('TempDelta (C)')
            st.write(selected['Temp_Delta_MinMax'].iloc[0])
        cola, colb, colc = st.columns(3)
        result, confidence = predict(st.session_state.scaled_features)
        with cola:
            st.write("Pluie demain?")
            if result ==True:
                st.write("☔")
            else:
                st.write(":sun_small_cloud:")
        with colb:
            st.write("Avec quelle pourcentage de confiance")
            st.text(confidence*100)
        with colc:
            st.write("Et la verité")
            truth = bool(st.session_state.actual_result.iloc[0])
            if truth ==True:
                st.write("☔")
            else:
                st.write(":sun_small_cloud:")
    
    st.markdown(
        """L'exactitude et la précision généralisées du modèle est discutée en détails dans la section « modélisation » de cette présentation. Ici, le plus utile – du point de vue de l’interprétation de la démonstration – est de savoir plus spécifiquement les faiblesses du modèle. C’est-à-dire : à quel point pouvons-nous faire confiance aux prédictions qui viennent de nous être présentées ? Le pourcentage de confiance est une première étape. Un pourcentage plus élevé montre une plus grande confiance du modèle que sa prédiction est correcte. Un pourcentage plus bas montre que la donnée est plus difficile à classer, et que le modèle à moins confiance en sa prédiction.
La matrice de confusion donne une idée de la fréquence à laquelle on prendra un parapluie pour rien, et de la même façon les occasions où il aurait été utile, mais avait été laissé sagement à la maison. Ceux qui aiment vivre dangereusement peuvent se fier immanquablement aux prédictions. Ceux d’une nature plus prudente pourront considérer de prendre un parapluie juste au cas où, les jours où la pluie n’est pas prédite, mais où la confiance est faible.
        """
    )
    conf_array = np.array([[25653/(25653+7237), 7237/(25653+7237)],[1899/(1899+7448),7448/(1899+7448)]])
    df = pd.DataFrame(conf_array, columns = ['prevision 0, pas de pluie', 'prevision 1, pluie'])
    col1, col2, col3 = st.columns([25,50,25])
    with col2:
        st.table(df)
    
    st.markdown(
        """
        La répétition de ce processus permet à l'utilisateur de remarquer soi-même l'influence des features les plus importantes. Cependant, il serait intéressant de pouvoir contrôler directement ces features, pour voir leur effet sur la prédiction. Les trois curseurs ci-dessous permettent de modifier la valeur des trois features sélectionnées (entre les valeurs minimum et maximum pour tout le dataset), et de voir si cela fait changer la prédiction finale du modèle.
        """
    )
    
#    Humidity_fiddled = st.slider('Humidity', 0.0,100.0,24.0)
#    Temp_fiddled = st.slider('TempDelta', -4.0, 26.0, 16.7)
#    Sunshine_fiddled = st.slider('Sunshine', 0.0,15.0,7.6)
    
    Humidity_fiddled = st.slider('Humidity', 0.0,100.0,63.0)
    Temp_fiddled = st.slider('TempDelta', -4.0, 26.0, 8.4)
    Sunshine_fiddled = st.slider('Sunshine', 0.0,15.0,5.1)
    
#    baseline = np.array([[0.0, Sunshine_fiddled, 33.0, Humidity_fiddled, 1030.0, 4.49925, 18.8, Temp_fiddled, -35.0, 0, 0, 1, 0]])
    baseline = np.array([[0.0, Sunshine_fiddled, 52.0, Humidity_fiddled, 1016.2, 7.0, 13.9, Temp_fiddled, -12.0, 0, 0, 0, 1]])
    column_names = ['Rainfall','Sunshine','WindGustSpeed','Humidity3pm','Pressure9am','Cloud3pm','Temp3pm','Temp_Delta_MinMax','Humidity_Delta','clim_chaud_humide','clim_méditerranéen','clim_sec','clim_tempéré_froid']
    fiddled_sample = pd.DataFrame(baseline, columns = column_names)
    
    cola, colb, colc = st.columns(3)
    fiddled_sample_scaled = scale_only(fiddled_sample)
    result_fiddled, confidence_fiddled = predict(fiddled_sample_scaled)
    with cola:
        st.write("Pluie demain?")
        if result_fiddled ==True:
            st.write("☔")
        else:
            st.write(":sun_small_cloud:")
    with colb:
        st.write("Avec quelle pourcentage de confiance")
        st.text(confidence_fiddled*100)
    
#    st.write(fiddled_sample)
#    if end:
#        pass
    #end while
