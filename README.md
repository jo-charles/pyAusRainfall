# pyAusRainfall / AVR22CDS : Prévisions météorologiques en Australie

## Présentation du projet
Ce projet porte sur l'étude d'une série chronologique regroupant environ 10 périodes d'observations météorologiques quotidiennes en Australie et couvre une gamme de techniques d'analyse, de modélisation et de prévision.

L'objectif principal est de prédire les précipitations du jour suivant l'observation à l'aide de la variable cible `"RainTomorrow"`. Une étude des prévisions de température pour le lendemain de l'observation et des prévisions à plus long terme sont également réalisées en évaluant des modèles de séries chronologiques.

Cette étude s'articule autour des étapes les plus importantes du processus décisonnel de la science des données:
>1. l'exploration, la visualisation et l'analyse des données,
>1. la préparation du jeu de données,
>1. l’élaboration et l’évaluation de modèles prédictifs,
>1. l'interprétabilité des modèles de classification étudiés,
>1. le déploiement du modèle retenu via une interface graphique.

Pour l’élaboration des modèles prédictifs, nous avons eu recours à:
>- des modèles de classification binaire avec apprentissage supervisé de type:
>    - régression logistique (“Logistic Regression”),
>    - forêts aléatoires (“Random Forest”),
>    - séparateurs à vaste marge (“Support Vector Machine”),
>    - K-plus proches voisins (“K-Nearest Neighbors”),
>    - arbres de décision (“Decision Tree”),
>- des modèles de séries temporelles multivariées.

## Contenu du GitHub
**01_Data_Visualization/**
- **[common_pyAusRainfall_dataviz.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/01_Data_Visualization/common_pyAusRainfall_dataviz.ipynb) :** 
> exploration, visualisation et analyse du jeu de données original

**02_Data_Preprocessing/**
- **[common_pyAusRainfall_features_selection.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/02_Data_Preprocessing/common_pyAusRainfall_features_selection.ipynb) :** 
> étude standalone de sélection des variables quantitatives
- **[common_pyAusRainfall_preprocessing.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/02_Data_Preprocessing/common_pyAusRainfall_preprocessing.ipynb) :** 
> préparation du jeu de données

**03_Data_Modeling/**
- **[common_pyAusRainfall_modelisation_with_resampling.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_modelisation_with_resampling.ipynb) :**
> étude de prévision de précipitations à J+1 par l'analyse de modèles de classification avec méthode de sous-échantillonnage
- **[common_pyAusRainfall_modelisation_without_resampling.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_modelisation_without_resampling.ipynb) :** 
> étude de prévision de précipitations à J+1 par l'analyse de modèles de classification sans méthode de sous-échantillonnage
- **[common_pyAusRainfall_temperature_forecasting.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_temperature_forecasting.ipynb) :** 
> étude standalone de prévision des températures par l'analyse du modèle de régression *"Gradient Boosting"*
- **[common_pyAusRainfall_time_series_by_climate_type.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_time_series_by_climate_type.ipynb) :** 
> analyse temporelle générale de la pluviométrie en fonction du type de climat
- **[common_pyAusRainfall_time_series_by_location.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_time_series_by_location.ipynb) :** 
> analyse temporelle de la pluviométrie à J+1, J+3 et J+7 en fonction d'une ville

**04_Model_Interpretability/**
- **[common_pyAusRainfall_DecisionTree.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_DecisionTree.ipynb) :**
> interprétabilité du modèle de classification *"Decision Tree"*
- **[common_pyAusRainfall_KNearestNeighbors.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_KNearestNeighbors.ipynb) :**
> interprétabilité du modèle de classification *"K-Nearest Neighbors"*
- **[common_pyAusRainfall_LogisticRegression.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_LogisticRegression.ipynb) :**
> interprétabilité du modèle de classification *"Logistic Regression"*
- **[common_pyAusRainfall_RandomForest.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_RandomForest.ipynb) :**
> interprétabilité du modèle de classification *"Random Forest"*
- **[common_pyAusRainfall_SupportVectorMachines.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_SupportVectorMachines.ipynb) :**
> interprétabilité du modèle de classification *"Support Vector Machines"*
    
**data/**
> stockage des différents jeux de données utilisés

**old/**
> contenu obsolète

**score/**
> stockage des scores obtenus par les différents modèles
    
**[GUIDELINES](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/GUIDELINES.md) :**
> consignes, répartition du travail et échéances des différentes itérations du projet
    
**[NOTES](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/NOTES.md) :**
> définition des variables, cadre méthodologique et suggestions d'améliorations (approches non considérées) 
    
## Source des données
> https://www.kaggle.com/jsphyg/weather-dataset-rattle-package

Le jeu de données étudié contient environ 10 ans d'observations météorologiques quotidiennes provenant de nombreux endroits en Australie, caractérisées par 23 variables explicatives météorologiques telles que la pression, la température, l'humidité, l'ensoleillement etc.

- Les observations proviennent de nombreuses stations météorologiques. Les observations quotidiennes sont disponibles sur http://www.bom.gov.au/climate/data
- Un exemple des dernières observations météorologiques à Canberra: http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml
- Définitions adaptées de http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml
- Source des données: http://www.bom.gov.au/climate/dwo/ et http://www.bom.gov.au/climate/data

## Rapport technique
> **[Rapport Technique d’évaluation](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/Rapport_PyAusRainfall_AVR22CDS.pdf)**

## Conditions de validation du projet
- Exploration des données (vision d’ensemble sur les données)
- Visualisations commentées et analysées
- Rapport technique + programmes + GitHub
- Une démonstration (Streamlit)
