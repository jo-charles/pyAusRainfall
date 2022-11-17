# pyAusRainfall / AVR22CDS : Prévisions météorologiques en Australie

## Présentation du projet
Ce projet considère une série temporelle couvrant une période d'environ 10 ans d'observations météorologiques quotidiennes en Australie et propose différentes techniques d'analyse, de modélisation et de prévision de valeurs futures. L'objectif principal consiste à prédire les précipitations au lendemain d'une observation à l'aide de la variable cible "RainTomorrow". Une étude de prévisions des températures au lendemain d'une observation est également réalisée ainsi que des prévisions à plus long terme par une évaluation de modèles de séries temporelles.

Ce projet s'articule autour de quatre axes:
1. l'exploration, la visualisation et l'analyse des données,
1. la préparation du jeu de données,
1. la modélisation (modèles de classification par apprentissage supervisé et modèles de séries temporelles),
1. l'interprétabilité des modèles de classification étudiés.

## Contenu du GitHub
**01_Data_Visualization/**
- **[common_pyAusRainfall_dataviz.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/01_Data_Visualization/common_pyAusRainfall_dataviz.ipynb) :** 
    - exploration, visualisation et analyse du jeu de données original

**02_Data_Preprocessing/**
- **[common_pyAusRainfall_features_selection.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/02_Data_Preprocessing/common_pyAusRainfall_features_selection.ipynb) :** 
    - étude standalone de sélection des variables quantitatives
- **[common_pyAusRainfall_preprocessing.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/02_Data_Preprocessing/common_pyAusRainfall_preprocessing.ipynb) :** 
    - préparation du jeu de données

**03_Data_Modeling/**
- **[common_pyAusRainfall_modelisation_with_resampling.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_modelisation_with_resampling.ipynb) :**
    - étude de prévision de précipitations à J+1 par l'analyse de modèles de classification avec méthode de sous-échantillonnage
- **[common_pyAusRainfall_modelisation_without_resampling.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_modelisation_without_resampling.ipynb) :** 
    - étude de prévision de précipitations à J+1 par l'analyse de modèles de classification sans méthode de sous-échantillonnage
- **[common_pyAusRainfall_temperature_forecasting.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_temperature_forecasting.ipynb) :** 
    - étude standalone de prévision des températures par l'analyse du modèle de régression *"Gradient Boosting"*
- **[common_pyAusRainfall_time_series_by_climate_type.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_time_series_by_climate_type.ipynb) :** 
    - analyse temporelle générale de la pluviométrie en fonction du type de climat
- **[common_pyAusRainfall_time_series_by_location.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_time_series_by_location.ipynb) :** 
    - analyse temporelle de la pluviométrie à J+1, J+3 et J+7 en fonction d'une ville

**04_Model_Interpretability/**
- **[common_pyAusRainfall_DecisionTree.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_DecisionTree.ipynb) :**
    - interprétabilité du modèle de classification *"Decision Tree"*
- **[common_pyAusRainfall_KNearestNeighbors.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_KNearestNeighbors.ipynb) :**
    - interprétabilité du modèle de classification *"K-Nearest Neighbors"*
- **[common_pyAusRainfall_LogisticRegression.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_LogisticRegression.ipynb) :**
    - interprétabilité du modèle de classification *"Logistic Regression"*
- **[common_pyAusRainfall_RandomForest.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_RandomForest.ipynb) :**
    - interprétabilité du modèle de classification *"Random Forest"*
- **[common_pyAusRainfall_SupportVectorMachines.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_SupportVectorMachines.ipynb) :**
    - interprétabilité du modèle de classification *"Support Vector Machines"*
    
**data/**
- stockage des différents jeux de données utilisés

**old/**
- contenu obsolète

**score/**
- stockage des scores obtenus par les différents modèles en format "*.csv"
    
**[GUIDELINES](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/GUIDELINES.md) :**
- consignes, répartition du travail et échéances des différentes itérations du projet
    
**[NOTES](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/NOTES.md) :**
- définition des variables, cadre méthodologique et suggestions d'améliorations  
    
## Source des données
https://www.kaggle.com/jsphyg/weather-dataset-rattle-package

Le jeu de données étudié contient environ 10 ans d'observations météorologiques quotidiennes provenant de nombreux endroits en Australie, caractérisées par 23 variables explicatives météorologiques telles que la pression, la température, l'humidité, l'ensoleillement etc.

- Les observations proviennent de nombreuses stations météorologiques. Les observations quotidiennes sont disponibles sur http://www.bom.gov.au/climate/data
- Un exemple des dernières observations météorologiques à Canberra: http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml
- Définitions adaptées de http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml
- Source des données: http://www.bom.gov.au/climate/dwo/ et http://www.bom.gov.au/climate/data

## Rapport technique
**[Rapport Technique d’évaluation](https://docs.google.com/document/d/1S6TrWBeBhRvBYoifv7e_KQCzcM46asP6mtodZ3nJNcE)**

## Conditions de validation du projet
- Exploration des données (vision d’ensemble sur les données)
- Visualisations commentées et analysées
- Rapport technique + programmes + GitHub
- Une démonstration (Streamlit)
