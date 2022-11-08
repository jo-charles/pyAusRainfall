# Prévisions météo en Australie

## Consignes de l'itération 1 : "Audit des données + DataViz"

    1. Fixer votre jeu de données et faire une analyse presque exhaustive de ce dernier
    2. Produire des visualisations pertinentes expliquant la structure, les difficultés et le biais du jeu de données 
    3. Accompagner le travail d'analyses statistiques de qualité

    Pour le rapport, préparer 1 notebook ou word/pdf contenant deux sous-parties:
        - Une partie rapport d'exploration des données dans lequel vous allez analyser et comprendre vos jeux de données 
        (nombre de données, longueur, présentation des colonnes, etc.)
        - Un rapport de visualisations pertinentes d'environ 3/4 pages contenant au moins 5 visualisations jolies et 
        pertinentes, à accompagner d'analyses statistiques de qualité

    Pour chaque visualisation:
        - Un commentaire précis, qui analyse la figure et apporte un avis "métier"
        - Une validation du constat par des manipulations de données, ou un test statistique

### Plan
    1. Préparation et nettoyage des données communes:
        • Observation du jeu de données initial
        • Ajout de variables supplémentaires
        • Gestion des NANs
        • Encoding
        • Exporter le jeu de données
    2. Etablir des axes d’intérêt pour les visualisations et les répartir:
        • Corrélation
        • Représentation cartographique
        • Moyenne annuelles des précipitations
        • Influence pour la prévision de pluie
        • Influence de certains critères (indépendamment du climat)
        • Influence de la pluie des jours précédents sur la pluie du lendemain
        • Influence des vents sur la pluie
        • Distribution des températures au cours de l’année suivant le climat
        • etc.
    3. Prévoir une session pour mettre en commun, nettoyer les codes et rédiger le rapport.

**Deadline:** Dimanche 3 juillet 2022

## Consignes de l'itération 2 : "Modélisation"

    1. Ajouter les coordonnées géographiques (Australia Cities Database | Simplemaps.com)
    2. Sélection des variables avec le test du chi2
    3. Extraction du jeu de données final
    4. Tableau des performances des algo avec et sans rééquilibrage
    5. Choisir une seconde stratégie pour l’itération 2 parmi les suivantes:
        • Classification des villes par clustering : création d'une nouvelle colonne catégorielle
        pour définir les différents types de climat selon les données climatiques
        • Deep Learning
        • Séries Temporelles
        • Pluie à J+3 et J+7
    
**Deadline:** Dimanche 11 septembre 2022
    
## Consignes de l'itération 3 : "Modélisation"

    1. Effectuer la même comparaison de performances sur la pluie à J+3 et J+7, et comparer
    2. Explorer les stratégies "Deep Learning" ou "Séries Temporelles"
    3. Tester différentes variables cibles telles que le vent ou la température

**Deadline:** Mercredi 28 septembre 2022

## Consignes de l'itération 4 : "Modélisation"
    1. Finaliser la modélisation: 
        • Derniers tests et modélisation:
            • Séries temporelles ARIMA
            • Séries temporelles et climats
            • Deep Learning
        • Comparer les performances des modèles et stratégies
        • Etablir les forces et faiblesses des modèles
        • Juger de l’interprétabilité du modèle retenu
        • Etablir les conclusions de la modélisation
        • Mettre au propre les codes sur GitHub
        • Support: rapport pdf ou word sur l’étape de modélisation
    2. Organiser le GitHub
    3. Rapport final: sous template que je vous fournirai la prochaine fois

### Répartition du travail
    • Joseph: 
        • Restructuration du repository et mise au propre des codes sur GitHub
        • Interprétabilité "SVM"
        • Amélioration du modèle de prédiction à J+3, J+7
    • Anne-Claire: 
        • Rédaction du pré-rapport final
        • Interprétabilité "Linear Regression"
    • Geneviève: 
        • Interprétabilité "Decision Tree"
        • Interprétabilité "Random Forest"
        • Modèle de prévision des températures
    • Olivier: 
        • Amélioration de l'étude "Time Series"
        • Interprétabilité "KNN"
        
**Synchro (interne):** Jeudi 13 octobre 2022 à 12h30 \
**Synchro:** Mardi 18 octobre 2022 à 17h30 \
**Deadline:** Mercredi 02 novembre 2022 à 17h30

## Consignes de l'itération 5 : "Rapport"
    1. Etablir les forces et faiblesses des modèles
    2. Juger de l’interprétabilité du modèle retenu
    3. Etablir les conclusions de la modélisation
    4. Structurer le repository GitHub en dossiers organisés
    5. Rédiger le rapport final à partir du template fourni 
        • Format du rapport: Google Docs 
        • Envoi du rapport: Lundi 05 décembre 2022 (retour en asynchrone le Mercredi 7 décembre 2022)
        • Deadline: Jeudi 15 décembre 2022

### Répartition du travail
    • Joseph: 
    • Anne-Claire: 
    • Geneviève: 
    • Olivier: 

**Synchro (interne):** Mardi 08 novembre 2022 à 17h30 \
**Deadline:** Lundi 19 décembre 2022 à 17h00

