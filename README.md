# pyAusRainfall : Prévisions météo en Australie

## Présentation du projet météo AVR22CDS
Cet ensemble de données contient environ 10 ans d'observations météorologiques quotidiennes provenant de nombreux endroits en Australie. Il y a donc différentes visualisations intéressantes possibles.
- Le premier objectif serait de prédire la variable cible "RainTomorrow". Elle signifie : a-t-il plu le jour suivant, oui ou non ? Cette colonne est Oui si la pluie pour ce jour était de 1mm ou plus. De même pour des prédictions de vent ou température.
- Dans un second temps, on pourra effectuer des prédictions à long terme, en utilisant des techniques mathématiques d’analyse de séries temporelles, et/ou des réseaux de neurones récurrents.

## Data
- https://www.kaggle.com/jsphyg/weather-dataset-rattle-package

## Définition des variables
- **Date** : Date d'observation.
- **Location** : Ville où se situe la station météorologique.
- **MinTemp** : Température minimale en degrés Celsius.
- **MaxTemp** : Température maximale en degrés Celsius.
- **Rainfall** : Quantité de pluie enregistrée pour la journée en millimètres.
- **Evaporation** : Niveau des bacs d'évaporation de classe A (en mm) dans les 24 heures jusqu'à 9h.
- **Sunshine** : Nombre d'heures d'ensoleillement dans la journée.
- **WindGustDir** : Direction des plus fortes rafales de vent dans les 24 heures jusqu'à minuit.
- **WindGustSpeed** : Vitesse en km/h des plus fortes rafales de vent dans les 24 heures jusqu'à minuit.
- **WindDir9am** : Direction du vent à 9h du matin.
- **WindDir3pm** : Direction du vent à 3h de l'après-midi.
- **WindSpeed9am** : Vitesse du vent en km/h moyennée sur 10 minutes avant 9h du matin.
- **WindSpeed3pm** : Vitesse du vent en km/h moyennée sur 10 minutes avant 3h de l'après-midi.
- **Humidity9am** : Humidité en pourcentage à 9h du matin.
- **Humidity3pm** : Humidité en pourcentage à 3h de l'après-midi.
- **Pressure9am** : Pression atmosphérique (hpa) au niveau de la mer à 9h.
- **Pressure3pm** : Pression atmosphérique (hpa) au niveau de la mer à 15h.
- **Cloud9am** : Opacité du ciel obscurci par les nuages à 9h mesuré en "oktas (0 signifie que le ciel est complètement éclairci tandis que 8 indique que le ciel est couvert.
- **Cloud3pm** : Opacité du ciel obscurci par les nuages à 15h mesuré en "oktas".
- **Temp9am** : Température en degrés Celsius à 9h du matin.
- **Temp3pm** : Température en degrés Celsius à 3h de l'après midi.
- **RainToday** : vaut 1 si les précipitations (en mm) dans les 24 heures avant 9h sont supérieur à 1mm, 0 sinon.
- **RainTomorrow** : vaut 1 si les précipitations (en mm) du lendemain sont supérieur à 1mm, 0 sinon.

## Notebooks utilisés
01_Data_Visualization:
- **"common_pyAusRainfall_dataviz.ipynb":** 
    - exploration et visualisation des données

02_Data_Preprocessing:
- **"common_pyAusRainfall_features_selection.ipynb":** 
    - étude standalone de sélection des variables
- **"common_pyAusRainfall_preprocessing.ipynb":** 
    - prétraitement des données

03_Data_Modeling:
- **"common_pyAusRainfall_modelisation_with_resampling.ipynb":**
    - contient les modélisations avec sous-échantillonnage
    - les scores sont résumés uniquement pour les modélisations avec sous-échantillonnage
- **"common_pyAusRainfall_modelisation_without_resampling.ipynb":** copie du fichier "common_pyAusRainfall_modelisation_with_resampling.ipynb" avec les particularités suivantes:
    - contient les modélisations sans sous-échantillonnage
    - les scores sont résumés pour les modélisations avec et sans sous-échantillonnage
- **"pyAusRainfall_short-term_forecasting.ipynb:"** 
    - étude des prévisions des précipitations à J+1, J+3 et J+7 par les méthodes des séries temporelles
- **"pyAusRainfall_Time_series.ipynb":** 
    - analyse temporelle de la pluviométrie
    
04_Model_Interpretability:
- **"common_pyAusRainfall_DecisionTree.ipynb":**
    - interprétabilité du modèle Decision Tree
- **"common_pyAusRainfall_knn.ipynb":**
    - interprétabilité du modèle KNN
- **"common_pyAusRainfall_Logistic_Regression.ipynb":**
    - interprétabilité du modèle Logistic Regression
    
## Benchmark / Bibliographie / Source
- Les observations proviennent de nombreuses stations météorologiques. Les observations quotidiennes sont disponibles sur http://www.bom.gov.au/climate/data.
- Un exemple des dernières observations météorologiques à Canberra: http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml
- Définitions adaptées de http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml
- Source des données: http://www.bom.gov.au/climate/dwo/ et http://www.bom.gov.au/climate/data

## Conditions de validation du projet
- Exploration des données (vision d’ensemble sur les données)
- Visualisations commentées et analysées
- Rapport technique + programmes + GitHub
- Une démo (Streamlit)
