# Prévisions météo en Australie

## Considérations actuelles
	• Variables ignorées: 
        • 'Date'
        • 'WindGustDir'
        • 'WindDir9am'
        • 'WindDir3pm'
	• Variables crées: 
        • 'Temp_Delta_MinMax'
        • 'Humidity_Delta'
        • 'clim_chaud_humide'
        • 'clim_méditerranéen'
        • 'clim_sec'
        • 'clim_tempéré_froid'
	• Variables dont les valeurs manquantes ont été supprimées:
        • 'RainToday'
        • 'RainTomorrow'

## Suggestions d'améliorations
	• Utilisation des variables catégorielles
	• Utilisation de Spark ML pour effectuer les algorithmes de classification tels que:
        • LogisticRegression() pour effectuer une régression logistique
        • DecisionTreeClassifier() pour un arbre de régression simple
        • RandomForestClassifier() pour une forêt aléatoire
        • LinearSVC() pour un SVM de régression à noyau linéaire