import streamlit as st

def app():
    st.title("Introduction")
    st.header("Contexte et explication des objectifs du projet")
    st.subheader("Prévisions météorologiques en Australie")
    st.markdown(
        """
Cet ensemble de données contient environ 10 ans d'observations météorologiques quotidiennes provenant de nombreux endroits en Australie. Il y a donc différentes visualisations intéressantes possibles.

- Le premier objectif serait de prédire la variable cible "RainTomorrow". Elle signifie : a-t-il plu le jour suivant, oui ou non ? Cette colonne est "Oui" si la pluie pour ce jour était de 1mm ou plus. De même pour des prédictions de vent ou température.
- Dans un second temps, on pourra effectuer des prédictions à long terme, en utilisant des techniques mathématiques d’analyse de séries temporelles, et/ou des réseaux de neurones récurrents.
    """
    )
   