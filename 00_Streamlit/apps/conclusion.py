import streamlit as st

def app():
    st.markdown("""<style>.normal-font {font-size:13.5pt}</style>""", unsafe_allow_html=True)
    st.title("Conclusion")
    st.header("Bilan")
    st.markdown("""
                <p class="normal-font">De manière générale, ce projet a permis à chacun de prendre en main certains outils dédiés à l’analyse, un langage de programmation et des méthodes applicables aux problèmes de données. La manipulation des algorithmes étudiés est complexe et cela a nécessité d’aller continuellement se documenter pour approfondir les connaissances acquises au cours de cette formation.
                """, unsafe_allow_html=True)
    st.header("Suggestions d'améliorations (approches non considérées)")
    st.markdown("""
                <p class="normal-font"> - relabellisation des données de la classe majoritaire en sous-classes pour obtenir un problème de classification multi-classes plus équilibré
                <p class="normal-font"> - utilisation de méthodes générant des sous-ensembles sous-échantillonnés, comme le Boosting ou le Bagging
                <p class="normal-font"> - utilisation des variables catégorielles ignorées dans le cadre de cette étude
                <p class="normal-font"> - utilisation d'autres méthodes de machine learning, comme l’Anomaly Detection ou l’Active Learning
                <p class="normal-font"> - utilisation de réseaux de neurones récurrents par des méthodes de Deep Learning avec "Keras"
                <p class="normal-font"> - utilisation de "Spark ML" afin d'optimiser les performances des algorithmes de classification tels que "Logistic Regression", "Decision Tree", "Random Forest" et "SVM"
                <p class="normal-font"> - Mise en place d'une pipeline avec barre de seuil
                """, unsafe_allow_html=True)