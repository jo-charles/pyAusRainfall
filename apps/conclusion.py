import streamlit as st


def app():
    st.title("Conclusion & Perspectives")
    st.header("Bilan")
    st.write("""En quoi votre projet a-t-il contribué à un accroissement de connaissance scientifique ?

De manière générale, ce projet a permis à chacun de prendre en main certains outils dédiés à l’analyse, un langage de programmation et des méthodes applicables aux problèmes de données. La manipulation des algorithmes étudiés est complexe et cela a nécessité d’aller continuellement se documenter pour approfondir les connaissances acquises au cours de cette formation.

Pour chacun des objectifs du projet, détaillez en quoi ils ont été atteints ou non.

Exploration, visualisation et analyse des données

L'étude statistique exploratoire réalisée a permis de nettoyer les données en vérifiant les doublons et les valeurs aberrantes et en remplaçant les valeurs manquantes. Les premières observations sur la signification de chaque variable par rapport à notre variable cible ont été obtenues à l’aide d’une matrice de corrélation. Comme la matrice de corrélation obtenue après encodage des variables qualitatives n'était pas satisfaisante, les variables catégorielles ont été ignorées pour ne garder que les variables quantitatives. Après sélection des variables quantitatives en fonction de leur importance par rapport à la variable cible, la matrice de corrélation obtenue a mis en évidence les variables fortement corrélées entre elles. Plusieurs visualisations ont été également réalisées pour valoriser les influences et distributions les plus importantes. 

Préparation du jeu de données

Cette étape s’appuie sur les constatations et conclusions obtenues lors de la première phase d’analyse exploratoire du jeu de données. Les variables catégorielles ont été écartées du jeu de données et les valeurs manquantes ont été remplacées en utilisant la méthode “KNN-Imputer” pour les variables présentant la plus forte proportion de valeurs manquantes et la méthode “interpolate” pour les variables présentant moins de 10% de valeurs manquantes. Les seules variables pour lesquelles les valeurs manquantes ont été supprimées sont “RainToday” et “RainTomorrow”. Les variables les moins corrélées à la variable cible ont été supprimées du jeu de données et différentes tables de contingences ont été produites afin de sélectionner, parmi les variables très corrélées entre elles, celle qui présente l’importance la plus élevée par rapport à la variable cible. Lors de cette étape, nous avons créé deux nouvelles variables qui nous semblaient pertinentes: “Temp_Delta_MinMax” et “Humidity_Delta”. De nouvelles variables spécifiant le type de climat australien selon 4 catégories ont également été créées. Enfin, la méthode “SelectKBest” a confirmé que toutes les variables que l’on considérait dans le cadre de cette étude étaient importantes à conserver. Différents jeux de données ont été générés et stockés afin de permettre l’accès à différentes configurations. Finalement, après avoir écarté les variables catégorielles, remplacé certaines variables trop fortement corrélées entre elles et ajouté de nouvelles variables explicatives, le jeu de données a subi une réduction significative de 3.2% des observations et de 39,1% des variables.

Elaboration et évaluation de modèles prédictifs

Une étude comparative de plusieurs modèles de classification binaire par apprentissage supervisé a été menée en se basant sur le choix de métriques d’évaluation appropriées aux jeux de données déséquilibrées. Cette étude compare différents modèles avec et sans méthode de rééchantillonnage. Chacune des approches établit les performances des métriques d’évaluation considérées (“f1_macro”, “balanced accuracy”, “geometric_mean” et “roc_auc”) en sélectionnant le meilleur estimateur parmi une grille de paramètres. Les différents résultats obtenus sont consolidés par validation croisée et accompagnés des courbes “ROC”, de “gain cumulé” et de “precision-rappel”. Une étude comparative basée sur la pondération des classes est effectuée pour tous les modèles (à l’exception du modèle KNN), et le seuil de probabilité est adapté dans toutes les modélisations pour mieux distinguer les classes.

Interprétabilité des modèles de classification étudiés

Pour chacun des modèles étudiés, nous avons proposé une approche d’interprétabilité en recourant à différentes techniques et visualisations qui viennent conforter le constat de départ sur l’importance relative des variables explicatives par rapport à notre variable cible. Cette étude nous apporte des informations complémentaires à celles obtenues lors de la phase de modélisation et qui nous aide à nous prononcer sur le choix d’un modèle final retenu.
"""
        )
   