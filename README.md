# pyAusRainfall : Prévisions météo en Australie

## Présentation du projet météo AVR22CDS
Cet ensemble de données contient environ 10 ans d'observations météorologiques quotidiennes provenant de nombreux endroits en Australie. Il y a donc différentes visualisations intéressantes possibles.
- Le premier objectif serait de prédire la variable cible : RainTomorrow. Elle signifie : a-t-il plu le jour suivant, oui ou non ? Cette colonne est Oui si la pluie pour ce jour était de 1mm ou plus. De même pour des prédictions de vent ou température.
- Dans un second temps, on pourra effectuer des prédictions à long terme, en utilisant des techniques mathématiques d’analyse de séries temporelles, et/ou des réseaux de neurones récurrents.

## Data
- https://www.kaggle.com/jsphyg/weather-dataset-rattle-package

## Définition des variables
- **Date** : Date d'observation.
- **Location** : Ville où se situe la station météorologique.
- **MinTemp** : Température minimale en degrés Celsius.
- **MaxTemp** : Température maximale en degrés Celsius.
- **Rainfall** : Quantité de pluie enregistrée pour la journée en millimètres.
- **Evaporation** : ***TO TRANSLATE**: The so-called Class A pan evaporation (mm) in the 24 hours to 9am*.
- **Sunshine** : Nombre d'heures d'ensoleillement dans la journée.
- **WindGustDir** : Direction des plus fortes rafales de vent dans les 24 heures jusqu'à minuit.
- **WindGustSpeed** : Vitesse en km/h des plus fortes rafales de vent dans les 24 heures jusqu'à minuit.
- **WindDir9am** : Direction du vent à 9h du matin.
- **WindDir3pm** : Direction du vent à 3h de l'après-midi.
- **WindSpeed9am** : Vitesse du vent en km/h moyennée sur 10 minutes avant 9h du matin.
- **WindSpeed3pm** : Vitesse du vent en km/h moyennée sur 10 minutes avant 3h de l'après-midi.
- **Humidity9am** : Humidité en pourcentage à 9h du matin.
- **Humidity3pm** : Humidité en pourcentage à 3h de l'après-midi.
- **Pressure9am** : ***TO TRANSLATE**: Atmospheric pressure (hpa) reduced to mean sea level at 9am*.
- **Pressure3pm** : ***TO TRANSLATE**: Atmospheric pressure (hpa) reduced to mean sea level at 3pm*.
- **Cloud9am** : ***TO TRANSLATE**: Fraction of sky obscured by cloud at 9am. This is measured in "oktas", which are a unit of eigths. It records how many eigths of the sky are obscured by cloud. A 0 measure indicates completely clear sky whilst an 8 indicates that it is completely overcast*.
- **Cloud3pm** : ***TO TRANSLATE**: Fraction of sky obscured by cloud (in "oktas": eighths) at 3pm. See Cload9am for a description of the values*.
- **Temp9am** : Température en degrés Celsius à 9h du matin.
- **Temp3pm** : Température en degrés Celsius à 3h de l'après midi.
- **RainToday** : ***TO TRANSLATE**: Boolean: 1 if precipitation (mm) in the 24 hours to 9am exceeds 1mm, otherwise 0*.
- **RainTomorrow** : ***TO TRANSLATE**: The amount of next day rain in mm. Used to create response variable RainTomorrow. A kind of measure of the "risk"*.

## Notebooks utilisés
- **"common_pyAusRainfall_dataviz.ipynb":** 
    - exploration et visualisation des données,
- **"common_pyAusRainfall_preprocessing.ipynb":** 
    - prétraitement des données,
- **"common_pyAusRainfall_features_selection.ipynb":** 
    - étude standalone de sélection des variables (**à approfondir**),
- **"common_pyAusRainfall_modelisation_with_resampling.ipynb":**
    - contient les modélisations avec sous-échantillonnage,
    - les scores sont résumés uniquement pour les modélisations avec sous-échantillonnage,
- **"common_pyAusRainfall_modelisation_without_resampling.ipynb":** copie du fichier "common_pyAusRainfall_modelisation_with_resampling.ipynb" avec les particularités suivantes:
    - contient les modélisations sans sous-échantillonnage,
    - les scores sont résumés pour les modélisations avec et sans sous-échantillonnage,
- **"pyAusRainfall_long-term_forecasting.ipynb:"** 
    - étude des prévisions à J+3 et J+7,
- **"pyAusRainfall_Time_series.ipynb":** 
    - analyse temporelle de la pluviométrie.

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
