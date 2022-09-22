# pyAusRainfall : Prévisions météo en Australie

## Présentation du projet météo AVR22CDS
Cet ensemble de données contient environ 10 ans d'observations météorologiques quotidiennes provenant de nombreux endroits en Australie. Il y a donc différentes visualisations intéressantes possibles.
- Le premier objectif serait de prédire la variable cible : RainTomorrow. Elle signifie : a-t-il plu le jour suivant, oui ou non ? Cette colonne est Oui si la pluie pour ce jour était de 1mm ou plus. De même pour des prédictions de vent ou température.
- Dans un second temps, on pourra effectuer des prédictions à long terme, en utilisant des techniques mathématiques d’analyse de séries temporelles, et/ou des réseaux de neurones récurrents.

## Data
- https://www.kaggle.com/jsphyg/weather-dataset-rattle-package

## Benchmark / Bibliographie / Source
- Les observations proviennent de nombreuses stations météorologiques. Les observations quotidiennes sont disponibles sur http://www.bom.gov.au/climate/data.
- Un exemple des dernières observations météorologiques à Canberra : http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml
- Définitions adaptées de http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml
- Source des données : http://www.bom.gov.au/climate/dwo/ et http://www.bom.gov.au/climate/data.

## Conditions de validation du projet
- Exploration des données (vision d’ensemble sur les données)
- Visualisations commentées et analysées
- Rapport technique + programmes + Github
- Une démo (Streamlit)
