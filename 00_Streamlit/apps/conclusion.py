import streamlit as st

def app():
    st.title("Conclusion")
    st.header("Bilan")
    st.write("""

    De manière générale, ce projet a permis à chacun de prendre en main certains outils dédiés à l’analyse, un langage de programmation et des méthodes applicables aux problèmes de données. La manipulation des algorithmes étudiés est complexe et cela a nécessité d’aller continuellement se documenter pour approfondir les connaissances acquises au cours de cette formation.
    """
        )
    st.title("Suggestions d'améliorations (approches non considérées)")
    st.write(""" 
    > - collecte de davantage de données pour éventuellement rééquilibrer les deux classes de la variable cible à un degré variable
    > - relabellisation des données de la classe majoritaire en sous-classes pour obtenir un problème de classification multi-classes plus équilibré
    > - utilisation des variables catégorielles ignorées dans le cadre de cette étude
    > - utilisation de méthodes générant des sous-ensembles sous-échantillonnés, comme le Boosting ou le Bagging
    > - utilisation d'autres méthodes de machine learning, comme l’Anomaly Detection ou l’Active Learning
    > - utilisation de réseaux de neurones récurrents par des méthodes de Deep Learning avec "Keras"
    > - utilisation de "Spark ML" afin d'optimiser les performances des algorithmes de classification tels que "Logistic Regression", "Decision Tree", "Random Forest" et "SVM"
    """)