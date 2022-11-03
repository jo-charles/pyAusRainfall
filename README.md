# pyAusRainfall : Prévisions météorologiques en Australie

## Présentation du projet météo AVR22CDS
Cet ensemble de données contient environ 10 ans d'observations météorologiques quotidiennes provenant de nombreux endroits en Australie. Il y a donc différentes visualisations intéressantes possibles.
- Le premier objectif serait de prédire la variable cible **"RainTomorrow"**. Elle signifie : a-t-il plu le jour suivant, oui ou non ? Cette colonne est Oui si la pluie pour ce jour était de 1mm ou plus. De même pour des prédictions de vent ou température.
- Dans un second temps, on pourra effectuer des prédictions à long terme, en utilisant des techniques mathématiques d’analyse de séries temporelles, et/ou des réseaux de neurones récurrents.

## Contenu du projet météo AVR22CDS
**01_Data_Visualization/**
- **[common_pyAusRainfall_dataviz.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/01_Data_Visualization/common_pyAusRainfall_dataviz.ipynb) :** 
    - exploration, visualisation et analyse des données.

**02_Data_Preprocessing/**
- **[common_pyAusRainfall_features_selection.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/02_Data_Preprocessing/common_pyAusRainfall_features_selection.ipynb) :** 
    - étude standalone de sélection des variables.
- **[common_pyAusRainfall_preprocessing.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/02_Data_Preprocessing/common_pyAusRainfall_preprocessing.ipynb) :** 
    - prétraitement des données.

**03_Data_Modeling/**
- **[common_pyAusRainfall_modelisation_with_resampling.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_modelisation_with_resampling.ipynb) :**
    - modélisations et scores associés avec méthode de sous-échantillonnage.
- **[common_pyAusRainfall_modelisation_without_resampling.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/common_pyAusRainfall_modelisation_without_resampling.ipynb) :** 
    - modélisations et scores associés sans méthode de sous-échantillonnage.
- **[pyAusRainfall_long-term_forecasting.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/pyAusRainfall_long-term_forecasting.ipynb) :** 
    - analyse temporelle de la pluviométrie à J+3 et J+7.
- **[pyAusRainfall_Time_series.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/03_Data_Modeling/pyAusRainfall_Time_series.ipynb) :** 
    - analyse temporelle générale de la pluviométrie.
    
**04_Model_Interpretability/**
- **[common_pyAusRainfall_DecisionTree.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_DecisionTree.ipynb) :**
    - interprétabilité du modèle Decision Tree.
- **[common_pyAusRainfall_Logistic_Regression.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_Logistic_Regression.ipynb) :**
    - interprétabilité du modèle Logistic Regression.
- **[common_pyAusRainfall_knn.ipynb](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/04_Model_Interpretability/common_pyAusRainfall_knn.ipynb) :**
    - interprétabilité du modèle KNN.
    
**data/**
- stockage des différents jeu de données utilisés.

**old/**
- contenu obsolète.

**score/**
- stockage des scores obtenus par les différents modèles.
    
**[GUIDELINES](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/GUIDELINES.md) :**
- consignes, répartition du travail et échéances des différentes itérations.
    
**[NOTES](https://github.com/DataScientest-Studio/pyAusRainfall/blob/main/NOTES.md) :**
- définition des variables, cadre méthodologique et suggestions d'améliorations.  
    
## Source des données
https://www.kaggle.com/jsphyg/weather-dataset-rattle-package

- Les observations proviennent de nombreuses stations météorologiques. Les observations quotidiennes sont disponibles sur http://www.bom.gov.au/climate/data.
- Un exemple des dernières observations météorologiques à Canberra: http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml.
- Définitions adaptées de http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml.
- Source des données: http://www.bom.gov.au/climate/dwo/ et http://www.bom.gov.au/climate/data.

## Rapport technique
https://docs.google.com/document/d/1S6TrWBeBhRvBYoifv7e_KQCzcM46asP6mtodZ3nJNcE

## Conditions de validation du projet
- Exploration des données (vision d’ensemble sur les données),
- Visualisations commentées et analysées,
- Rapport technique + programmes + GitHub,
- Une démo (Streamlit).
