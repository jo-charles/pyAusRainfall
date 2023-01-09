import streamlit as st

def app():
    st.title("Le dataset")
    st.header("Cadre")
    st.subheader("Quel(s) jeu(x) de donnée(s) avez vous utilisé pour atteindre les objectifs de votre projet ?")    
    st.write(
    """
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
    - RainTomorrow : vaut 1 si les précipitations (en mm) du lendemain sont supérieur à 1 mm, 0 sinon""")              
             