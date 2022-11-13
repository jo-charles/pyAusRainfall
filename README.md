# pyAusRainfall : Prévisions météorologiques en Australie

## Présentation du projet météo AVR22CDS
Cet ensemble de données contient environ 10 ans d'observations météorologiques quotidiennes provenant de nombreux endroits en Australie. Il y a donc différentes visualisations intéressantes possibles.
- Le premier objectif serait de prédire la variable cible **"RainTomorrow"**. Elle signifie : a-t-il plu le jour suivant, oui ou non ? Cette colonne est "Oui" si la pluie pour ce jour était de 1mm ou plus. De même pour des prédictions de vent ou température.
- Dans un second temps, on pourra effectuer des prédictions à long terme, en utilisant des techniques mathématiques d’analyse de séries temporelles, et/ou des réseaux de neurones récurrents.

## Contenu du projet météo AVR22CDS
**01_Data_Visualization/**
- **[common_pyAusRainfall_dataviz.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/01_Data_Visualization/common_pyAusRainfall_dataviz.ipynb) :** 
    - exploration, visualisation et analyse du jeu de données original

**02_Data_Preprocessing/**
- **[common_pyAusRainfall_features_selection.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/02_Data_Preprocessing/common_pyAusRainfall_features_selection.ipynb) :** 
    - étude standalone de sélection des variables quantitatives
- **[common_pyAusRainfall_preprocessing.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/02_Data_Preprocessing/common_pyAusRainfall_preprocessing.ipynb) :** 
    - prétraitement du jeu de données original

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
