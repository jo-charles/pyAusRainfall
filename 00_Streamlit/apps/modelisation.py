import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import io

from PIL import Image

# Choix des modèles → Modélisation
# formuler le pb de ML
# Présenter les modèles qui n’ont pas marché (viz comparative des performances)

# agree = st.checkbox('I agree')
# if agree:
#    st.write('Great!')

# st.success('This is a success message!', icon="✅")

def app():
    models = ["Régression logistique (Logistic Regression)", 
          "Forêts aléatoires (Random Forest)", 
          "Séparateurs à vaste marge (Support Vector Machine)", 
          "K-plus proches voisins (K-Nearest Neighbors)", 
          "Arbres de décision (Decision Tree)"]

    model_descriptions = {
        "Régression logistique (Logistic Regression)": 
        "La régression logistique est un modèle statistique utilisé pour résoudre les problèmes de classification binaire. Il permet de prédire une probabilité de pertinence pour chaque classe en utilisant une fonction logistique. Ce modèle est souvent utilisé dans les contextes de classification de données binaires telles que la détection de spam ou la prédiction de l'échec d'un crédit. Cependant, il est moins interprétable que d'autres modèles tels que les arbres de décision car il ne donne pas une idée claire des caractéristiques qui ont conduit à la prédiction.",
        "Forêts aléatoires (Random Forest)":
        "Les forêts aléatoires sont un ensemble d'arbres de décision formant un ensemble d'apprentissage supervisé. Il permet de maximiser les chances de prédire correctement la variable cible, car il s’appuie sur l’ensemble des prédictions des différents arbres pour faire une prédiction. Ces modèles sont souvent utilisés pour les problèmes de classification multi-classes ou de régression. Ils offrent également la possibilité de mesurer l'importance relative des variables, permettant une meilleure interprétabilité des résultats.",
        "Séparateurs à vaste marge (Support Vector Machine)":
        "Les séparateurs à vaste marge sont un modèle de classification supervisée utilisant des fonctions de noyau pour séparer les données dans l'espace de caractéristiques. Ils sont souvent utilisés pour les jeux de données non linéaires ou pour des problèmes de classification multi-classes. Cependant, ils peuvent être sensibles aux données bruyantes et ont des difficultés à gérer les données très déséquilibrées",
        "K-plus proches voisins (K-Nearest Neighbors)":
        "Le modèle des K-plus proches voisins est un modèle de classification supervisée qui utilise la distance euclidienne pour classer les nouvelles observations en fonction de leurs K plus proches voisins dans l'ensemble d'apprentissage. Il est souvent utilisé pour la classification de données à des fins de reconnaissance d'images ou de reconnaissance vocale. Il est facile à comprendre et à implémenter mais peut être lent pour des jeux de données volumineux.",
        "Arbres de décision (Decision Tree)":
        "Les arbres de décision sont des modèles de classification et de régression utilisés pour résoudre des problèmes de machine learning supervisés. Ils sont basés sur une structure hiérarchique de questions (nœuds) et de réponses (feuilles) qui permettent de faire des prédictions à partir d'une variable cible. Les arbres de décision sont souvent utilisés pour résoudre des problèmes de classification binaire et multi-classes, ainsi que pour l'analyse de données de type régression. Les arbres de décision sont souvent très interprétables car ils permettent de visualiser les règles de décision prises par le modèle. Cependant, ils peuvent être sujets à surapprentissage lorsque la complexité du modèle est trop élevée."
    }
    
    ts_models = ["ARIMA (Auto-Regressive Integrated Moving Average)", 
         "SARIMA (Seasonal Auto-Regressive Integrated Moving Average)"]

    ts_model_descriptions = {
        "ARIMA (Auto-Regressive Integrated Moving Average)": 
        "Le modèle ARIMA (Auto-Regressive Integrated Moving Average) est un modèle statistique utilisé pour l'analyse et la prévision des séries chronologiques. Il combine des modèles d'autorégression (AR), de différenciation (I) et de moyenne mobile (MA) pour comprendre les tendances et saisonnalités dans les données. Il est souvent utilisé pour prévoir des événements tels que les ventes, les émissions de gaz à effet de serre, la consommation énergétique, etc.",
        "SARIMA (Seasonal Auto-Regressive Integrated Moving Average)":
        "Le modèle SARIMA (Seasonal Auto-Regressive Integrated Moving Average) est une extension de l'ARIMA qui prend en compte les tendances saisonnières dans les données. Il est utilisé pour les séries chronologiques avec des tendances saisonnières, comme les données de vente au détail, de tourisme, de météo, etc. C'est un outil efficace pour la détection des tendances saisonnières et l'analyse des tendances de fond dans les données."
    }
    
    st.title("Modélisation des données")
    st.header("Type de problème de machine learning")
    st.subheader("Classification binaire par apprentissage supervisé")
    st.markdown("""
Ce projet vise à résoudre un défi de classification binaire en utilisant des techniques d'apprentissage supervisé. Il s'agit de prévoir la valeur d'une variable cible quantitative en utilisant des données étiquetées qui comprennent des entrées et des sorties. Grâce à ces étiquettes, le modèle peut évaluer son exactitude et continuer à s'améliorer au fil du temps. En utilisant des techniques d'apprentissage supervisé, le modèle est capable de généraliser à de nouvelles données, en s'appuyant sur les connaissances acquises lors de l'entraînement.

Pour l’élaboration de modèles prédictifs, nous avons utilisé différents modèles de classification binaire, tels que la régression logistique, les forêts aléatoires, les séparateurs à vaste marge, les K-plus proches voisins, et les arbres de décision. Ces modèles utilisent des algorithmes différents pour la prédiction de la variable cible, et nous les avons comparés pour déterminer le meilleur modèle pour résoudre notre problème de classification binaire.
""")
    model_selected = st.radio("", models, label_visibility="collapsed")
    st.write(":information_source:", model_descriptions[model_selected])
 
    st.markdown("""
Le jeu de données utilisé dans ce projet est une série temporelle multivariée, c'est-à-dire qu'il regroupe l'évolution temporelle de plusieurs variables explicatives. Cela permet la détection de corrélations entre ces variables au fil du temps. Pour gérer ce type de données, nous avons considéré différents modèles de séries temporelles multivariées. Ces modèles incluent des techniques de décomposition de séries temporelles pour isoler les tendances, les saisons et les résidus des séries.
""")
    ts_model_selected = st.radio("", ts_models, label_visibility="collapsed")
    st.write(":information_source:", ts_model_descriptions[ts_model_selected])
    
    st.subheader("Classification de données déséquilibrées")
    st.markdown("""
Ce projet se concentre sur la classification de données déséquilibrées, similaire à la détection d'anomalies. Pour traiter les données déséquilibrées, nous avons recours à des techniques de sous-échantillonnage et sur-échantillonnage pour rééquilibrer les données et sélectionner la méthode la plus efficace en fonction des métriques choisies. La technique du sous-échantillonnage "RandomUnderSampler" a été utilisée car elle s'est avérée la plus performante étant donné l'ampleur de notre ensemble de données (145,460 observations) et les conséquences sur les performances de certains algorithmes.
""")

    # Données pour le camembert
    data = {'Classe 0 : 78%': 78, 'Classe 1 : 22%': 22}

    # Génération du graphique
    plt.pie(data.values(), labels=data.keys())

    # Convertir en une image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    im = Image.open(buf)

    col1, col2 = st.columns(2)
    
    # Afficher l'image
    col1.image(im, width=500, caption="Répartition des classes de la variable cible \"RainTomorrow\" sur toutes les observations du jeu de données original")
      
    data = {
        "Ensemble d'entraînement": {'class 0': 76696, 'class 1': 21854},
        "Ensemble d'entraînement ré-échantillonné": {'class 0': 21854, 'class 1': 21854},
        "Ensemble de test": {'class 0': 32890, 'class 1': 9347}
    }

    fig = go.Figure()
    colors = {"Ensemble d'entraînement": ['blue', 'blue'], "Ensemble d'entraînement ré-échantillonné": ['purple', 'purple'],"Ensemble de test": ['orange', 'orange']}
    for name, value in data.items():
        fig.add_trace(go.Bar(x=list(value.keys()), y=list(value.values()), name=name,
                            marker=dict(color=colors[name])))

    fig.update_layout(barmode='group')
    col2.plotly_chart(fig)
    
    st.subheader("Classification pénalisée")
    st.markdown("""
La classification pénalisée est une technique utilisée pour traiter les cas de données déséquilibrées. Elle permet d’appliquer des coûts supplémentaires au modèle pour les erreurs de classification commises sur la classe minoritaire pendant l'entraînement. Ces pénalités sur les erreurs ont pour objectif d'inciter les modèles à accorder plus d'attention à la classe minoritaire, afin de réduire les biais dans les prédictions.

Un des moyens courant pour mettre en place cette technique est d'utiliser l'argument "balanced" lors de la définition du modèle, ce qui permet d'attribuer à chaque classe un poids inversement proportionnel à sa fréquence d'apparition dans les données d'entraînement. Pour aller plus loin nous avons également testé différents ratios sur les classes pour déterminer la configuration qui donne les meilleurs résultats par rapport aux métriques principales et secondaires.

En complément, nous avons ajusté le seuil de probabilité à partir duquel les prédictions sont classées comme positives ou nulles, c'est-à-dire la valeur seuil à partir de laquelle un individu sera classé dans la classe majoritaire ou la classe minoritaire. Ajuster ce seuil de manière optimale nous permet de marquer plus distinctement les classes et d'améliorer les performances de notre modèle.
""")

    metrics = ["f1_score", "f1_micro", "f1_weighted", "f1_macro"]
    metrics_descriptions = {
        "f1_score": 
        "La métrique de performance **f1_score**, également appelée moyenne harmonique entre la précision et le rappel, est un outil couramment utilisé pour évaluer les performances d'un modèle de classification. Elle est calculée en faisant la moyenne harmonique entre la précision (taux de prédictions positives correctes) et le rappel (taux de positifs correctement prédits). Les avantages de l'utilisation de la métrique F1-score incluent sa capacité à prendre en compte à la fois la précision et le rappel, ainsi qu'à être particulièrement adaptée pour les jeux de données déséquilibrées. En effet, elle donne une idée de la qualité globale de la classification en pondérant les performances des différentes classes. Cependant, il y a aussi des inconvénients à utiliser cette métrique, tels que sa sensibilité aux données déséquilibrées et son manque d'indication sur les performances de chaque classe spécifique.",
        "f1_micro":
        "La métrique de performance **f1_micro** est une variante de la métrique f1_score qui calcule une seule valeur globale pour l'ensemble des données en tenant compte de toutes les observations, indépendamment de la classe à laquelle elles appartiennent. Cette métrique est particulièrement utile dans les cas où la classe minoritaire est très petite et où la métrique f1_score peut être biaisée. Les avantages de cette métrique sont qu'elle donne une idée de la qualité globale de la classification, qu'elle est particulièrement adaptée pour les jeux de données déséquilibrés et qu'elle prend en compte toutes les observations. Cependant, cette métrique a des inconvénients, comme le fait qu'elle ne donne pas d'indication sur les performances de chaque classe spécifique et qu'elle peut être sensible aux données déséquilibrées.",
        "f1_weighted": 
        "La métrique de performance **f1_weighted** est une variante de la métrique f1_score qui prend en compte la répartition des classes dans les données. Elle calcule la moyenne pondérée des f1_score pour chaque classe en utilisant le nombre d'exemples de chaque classe comme poids. Cette métrique est utile dans les cas où les classes ont des tailles très différentes et où il est important de considérer les performances pour chaque classe spécifique. Les avantages de cette métrique sont qu'elle tient compte de la répartition des classes dans les données et qu'elle est utile lorsque les classes ont des tailles très différentes. Cependant, cette métrique a l'inconvénient de pouvoir survaloriser les classes plus grandes si les performances pour les classes plus petites sont faibles.",
        "f1_macro":
        "La métrique de performance **f1_macro** est une méthode d'évaluation de la performance des modèles de classification qui calcule la moyenne des f1_scores pour chaque classe, sans tenir compte de la répartition des classes dans les données. Cette métrique est particulièrement utile lorsque les classes ont des tailles similaires et que l'on souhaite connaître la performance moyenne pour chaque classe. Cependant, elle peut sous-estimer la performance globale si certaines classes ont des tailles très différentes et elle ne tient pas compte de la répartition des classes dans les données. En utilisant cette métrique, nous pourrons évaluer la performance moyenne pour chaque classe dans nos modèles de classification, mais il est important de considérer également d'autres métriques pour obtenir une vision complète de la performance de notre modèle. Il est également important de considérer les données déséquilibrées, c'est pourquoi il est souvent utile de combiner cette métrique avec d'autres métriques comme le f1_micro, qui calcule une seule valeur globale en considérant l'ensemble des données, ou le f1_weighted, qui calcule une moyenne pondérée des f1_scores pour chaque classe en tenant compte de la répartition des classes dans les données. Cela permet de prendre en compte les performances sur les classes minoritaires tout en prenant en compte la répartition des classes dans les données, pour obtenir une vision plus complète et précise des performances de notre modèle."
    }    
    metrics_expressions = {
        "f1_score":
        "$\\text{f1\_score} = \\frac{2\,*\,precision\,*\,recall}{precision\,+\,recall}$",
        "f1_micro":
        "$\\text{f1\_micro} = \\frac{2\,*\,TP}{2\,*\,TP\,+\,FN\,+\,FP}$",
        "f1_weighted":
        "$\\text{f1\_weighted} = \\frac{\sum_{i=1}^{n} w_i * f1_i}{\sum_{i=1}^{n} w_i}$",
        "f1_macro":
        "$\\text{f1\_macro} = \\frac{\\sum_{i=1}^n f1_{class\_i}}{n}$",
    }
    
    st.subheader("Métrique de performance principale")
    st.markdown("""
Lorsque l'on travaille sur un jeu de données de classification binaire déséquilibré, il est crucial d'utiliser des métriques de performance appropriées pour évaluer les performances de notre modèle. Pour évaluer les performances de ces modèles, des mesures de performance comme l'accuracy, le f1_score, la précision et le rappel ont été utilisées. Cependant, il est important de noter que ces mesures ne donnent pas une image complète de la performance du modèle car elles sont souvent biaisées en faveur de la classe majoritaire. C'est pourquoi il est important d'utiliser des métriques de performance secondaires pour obtenir une vision complète des performances de nos modèles. \n

Parmi les métriques de performance secondaires couramment utilisées pour les jeux de données déséquilibrés, la métrique **f1_macro** est particulièrement judicieuse en tant que métrique de performance principale. Cette métrique calcule la moyenne arithmétique du **f1_score** pour chaque classe, en traitant ainsi toutes les classes de la même manière, quelle que soit leur distribution. Cette métrique est particulièrement adaptée pour les situations de classes déséquilibrées, car elle est indépendante de la répartition des classes dans les données. En plus de donner une idée plus précise des performances de notre modèle en prenant en compte les erreurs de classification pour les classes minoritaires, elle permet également de mieux comprendre les performances de chaque classe spécifique, ce qui est crucial pour pouvoir identifier les lacunes de performance pour les classes minoritaires. 
""")
    
    metric_selected = st.radio("", metrics, label_visibility="collapsed")
    st.write(":information_source:", metrics_descriptions[metric_selected])
    st.write(":pencil2:", metrics_expressions[metric_selected])
    
    sec_metrics = ["balanced_accuracy", "geometric_mean", "roc_auc"]
    sec_metrics_descriptions = {
        "balanced_accuracy": 
        "La métrique de performance **balanced accuracy** est une alternative à l'accuracy standard qui prend en compte la répartition des classes dans les données. Elle calcule la moyenne arithmétique de la sensibilité et de la spécificité pour chaque classe, plutôt que de les combiner comme c'est le cas avec l'accuracy standard. Cette méthode permet d'évaluer la performance du modèle de manière plus équilibrée, en prenant en compte les performances de chaque classe, indépendamment de leur répartition dans les données. Cette métrique est particulièrement adaptée pour les jeux de données déséquilibrés, car elle évite de surestimer les performances pour les classes majoritaires en calculant la précision moyenne pour chaque classe en tenant compte de leur distribution. Les avantages de cette métrique sont qu'elle est particulièrement adaptée pour les jeux de données déséquilibrés et qu'elle donne une idée de la qualité globale de la classification. Elle est également utile pour les cas où il est important de prendre en compte les performances de chaque classe indépendamment de leur répartition dans les données. Cependant, cette métrique a également des inconvénients. Elle peut sous-estimer les performances globales si certaines classes ont des tailles très différentes et qu'elle peut ne pas tenir compte de la répartition des classes dans les données. Il est donc important de considérer d'autres métriques telles que la sensibilité, la spécificité et d'autres métriques de performance plus appropriées pour les jeux de données déséquilibrés.",
        "geometric_mean":
        "La métrique de performance **geometric_mean** est une approche pour évaluer les performances d'un modèle de classification en tenant compte de la répartition des classes dans les données. Elle calcule la racine carrée du produit des sensibilités pour chaque classe, ce qui permet d'avoir une vue équilibrée de la performance pour chacune d'entre elles. Elle est particulièrement utile pour les jeux de données déséquilibrés, car elle permet de maximiser la précision pour chaque classe tout en maintenant un équilibre entre les performances de chaque classe. La métrique geometric_mean permet également de prendre en compte les performances pour chaque classe en tenant compte de leur distribution. Elle est particulièrement adaptée pour les jeux de données déséquilibrés, car elle tente de maximiser la précision pour chaque classe tout en maintenant un équilibre global. Les avantages de cette métrique sont qu'elle permet de prendre en compte la répartition des classes dans les données, elle est particulièrement adaptée pour les jeux de données déséquilibrés et qu'elle permet de maximiser les performances pour chaque classe tout en maintenant un équilibre entre les performances des différentes classes. Les inconvénients sont qu'elle peut être sensible aux données déséquilibrées et qu'elle peut ne pas être adaptée pour tous les types de données. Il est donc important de combiner l'utilisation de cette métrique avec d'autres métriques de performance secondaires pour obtenir une image complète des performances de notre modèle.",
        "roc_auc": 
        "La métrique de performance roc_auc (Receiver Operating Characteristic - Area Under the Curve) est une mesure utilisée pour évaluer les modèles de classification binaire qui prend en compte le compromis entre les taux de vrais positifs et les taux de faux positifs pour un modèle donné. Elle utilise la courbe ROC (Receiver Operating Characteristic) qui représente les taux de VP en fonction des taux de FP pour visualiser les performances d'un modèle pour différents seuils de classification. L'AUC (Area Under the Curve) est ensuite utilisée pour quantifier ces performances en un seul score numérique. Cette métrique est particulièrement utile pour les jeux de données déséquilibrées car elle prend en compte la distribution des classes dans les données et permet de mieux comprendre les performances d'un modèle en termes de capacité à détecter les cas positifs. Il est cependant important de noter qu'elle peut être sensible aux données déséquilibrées, car un petit nombre de prédictions correctes/incorrectes peut entraîner une grande variation du score. Les avantages de cette métrique sont qu'elle est indépendante du seuil de classification et qu'elle donne une idée de la performance globale d'un modèle. Elle est particulièrement utile pour les jeux de données déséquilibrées, où il est souvent difficile de trouver un seuil de classification optimal. Les inconvénients de cette métrique sont qu'elle peut être sensible aux variations de la distribution des données et qu'elle ne donne pas d'indication sur les performances de chaque classe spécifique. Pour pallier à cela, il est également important de considérer les autres métriques telles que la sensibilité et la spécificité, ainsi que d'autres métriques de performance plus appropriées pour les jeux de données déséquilibrées, telles que les métriques f1_micro ou geometric_mean. Il est également important de consulter les courbes ROC pour visualiser les performances de modèles sur une plage de seuils de probabilité et de considérer les facteurs tels que l'équité et la robustesse dans l'évaluation globale des modèles. Il est donc important de combiner l'AUC-ROC avec d'autres métriques et techniques d'évaluation pour obtenir une analyse complète des performances de notre modèle."
    }        
    sec_metrics_expressions = {
        "balanced_accuracy":
        "$\\text{balanced\_accuracy} = \\frac{sensibilité + spécificité}{2}$",
        "geometric_mean":
        "$\\text{geometric\_mean} = \sqrt{\prod_{i=1}^{n} Sensitivity_i}$",
        "roc_auc":
        "$\\text{roc\_auc} = \\frac{1 + Sensitivity - Specificity}{2}$"
    }
    
    st.subheader("Métriques de performance secondaires")
    
    st.markdown("""
    Dans le cadre de la modélisation d'un problème de classification binaire sur jeu de données déséquilibré, il est crucial d'utiliser des métriques de performance secondaires pour évaluer les performances de notre modèle. La métrique de performance **f1_macro** est couramment utilisée pour les jeux de données déséquilibrées car elle calcule la moyenne arithmétique du **f1_score** pour chaque classe, indépendamment de leur distribution. Cependant, elle ne donne pas d'indication sur les performances de chaque classe spécifique et peut sous-estimer les performances globales si certaines classes ont des tailles très différentes. Il est donc important de la combiner avec d'autres métriques pour avoir une analyse plus complète des performances du modèle.
""")
    
    sec_metric_selected = st.radio("", sec_metrics, label_visibility="collapsed")
    st.write(":information_source:", sec_metrics_descriptions[sec_metric_selected])
    st.write(":pencil2:", sec_metrics_expressions[sec_metric_selected])
    
    st.subheader("Evaluation de modèles prédictifs")

    st.markdown("""
Une étude comparative de plusieurs modèles de classification binaire par apprentissage supervisé a été menée en
se basant sur le choix de métriques d’évaluation appropriées aux jeux de données déséquilibrées. Cette étude
compare différents modèles avec et sans méthode de rééchantillonnage. Chacune des approches établit les
performances des métriques d’évaluation considérées ("f1_macro", "balanced accuracy", "geometric_mean" et
"roc_auc") en sélectionnant le meilleur estimateur parmi une grille de paramètres. Les différents résultats obtenus
sont consolidés par validation croisée et accompagnés des courbes "ROC", de "gain cumulé" et de
"precision-rappel". Une étude comparative basée sur la pondération des classes est effectuée pour tous les
modèles (à l’exception du modèle KNN), et le seuil de probabilité est adapté dans toutes les modélisations pour
mieux distinguer les classes. 
""")

    st.markdown("""
Les meilleures performances obtenues correspondent aux modélisations des prévisions des précipitations avec étape de rééchantillonnage. Elles sont résumées dans le tableau suivant :
""") 
    img = Image.open("images/scores_with_resampling.png")
    st.image(img, width=600, caption="Performances des différents algorithmes obtenus après sous-échantillonage des données")
    
    st.warning("""
Pour chaque algorithme considéré (à l’exception du modèle knn), les index 1, 2 et 3 représentent les différentes
itérations d’une étude comparative basée sur la pondération des classes, à savoir:
- 0 : correspond au paramétrage "class_weight = None" dans la définition du modèle
- 1 : correspond au paramétrage "class_weight = 'balanced'" dans la définition du modèle
- 2 : correspond au paramétrage "class_weight = {0\:x, 1\:1-x}" dans la définition du modèle
De plus, le seuil de probabilité est adapté automatiquement dans toutes les modélisations afin de mieux distinguer les classes.    
""", icon="⚠️")