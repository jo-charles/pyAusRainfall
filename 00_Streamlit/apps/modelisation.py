import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import io

from PIL import Image

def app():
    st.title("Modélisation des données")
    st.header("Formulation du problème de Machine Learning")
    st.subheader("Classification binaire par apprentissage supervisé")
    st.markdown("""
Ce projet vise à résoudre un problème de classification binaire en utilisant des techniques d'apprentissage supervisé. Il s'agit de prévoir la valeur d'une variable cible quantitative en utilisant des données étiquetées qui comprennent des entrées et des sorties. Grâce à ces étiquettes, le modèle peut évaluer son exactitude et continuer à s'améliorer au fil du temps. En utilisant des techniques d'apprentissage supervisé, le modèle est capable de généraliser à de nouvelles données, en s'appuyant sur les connaissances acquises lors de l'entraînement.

Pour l'élaboration de modèles prédictifs, nous avons utilisé différents modèles de classification binaire, tels que la régression logistique, les forêts aléatoires, les séparateurs à vaste marge, les K-plus proches voisins, et les arbres de décision. Ces modèles utilisent des algorithmes différents pour la prédiction de la variable cible, et nous les avons comparés pour déterminer le meilleur modèle pour résoudre notre problème de classification binaire.
""")
    
    models = ["Régression logistique (Logistic Regression)", 
          "Forêts aléatoires (Random Forest)", 
          "Séparateurs à vaste marge (Support Vector Machine)", 
          "K-plus proches voisins (K-Nearest Neighbors)", 
          "Arbres de décision (Decision Tree)"]

    model_descriptions = {
        "Régression logistique (Logistic Regression)": 
        "La **régression logistique** est un modèle statistique utilisé pour résoudre les problèmes de classification binaire. Il permet de prédire une probabilité de pertinence pour chaque classe en utilisant une fonction logistique. Ce modèle est souvent utilisé dans les contextes de classification de données binaires telles que la détection de spam ou la prédiction de l'échec d'un crédit. Cependant, il est moins interprétable que d'autres modèles tels que les arbres de décision car il ne donne pas une idée claire des caractéristiques qui ont conduit à la prédiction.",
        "Forêts aléatoires (Random Forest)":
        "Les **forêts aléatoires** sont un ensemble d'arbres de décision formant un ensemble d'apprentissage supervisé. Il permet de maximiser les chances de prédire correctement la variable cible, car il s’appuie sur l’ensemble des prédictions des différents arbres pour faire une prédiction. Ces modèles sont souvent utilisés pour les problèmes de classification multi-classes ou de régression. Ils offrent également la possibilité de mesurer l'importance relative des variables, permettant une meilleure interprétabilité des résultats.",
        "Séparateurs à vaste marge (Support Vector Machine)":
        "Les **séparateurs à vaste marge** sont un modèle de classification supervisée utilisant des fonctions de noyau pour séparer les données dans l'espace de caractéristiques. Ils sont souvent utilisés pour les jeux de données non linéaires ou pour des problèmes de classification multi-classes. Cependant, ils peuvent être sensibles aux données bruyantes et ont des difficultés à gérer les données très déséquilibrées",
        "K-plus proches voisins (K-Nearest Neighbors)":
        "Le modèle des **K-plus proches voisins** est un modèle de classification supervisée qui utilise la distance euclidienne pour classer les nouvelles observations en fonction de leurs K plus proches voisins dans l'ensemble d'apprentissage. Il est souvent utilisé pour la classification de données à des fins de reconnaissance d'images ou de reconnaissance vocale. Il est facile à comprendre et à implémenter mais peut être lent pour des jeux de données volumineux.",
        "Arbres de décision (Decision Tree)":
        "Les **arbres de décision** sont des modèles de classification et de régression utilisés pour résoudre des problèmes de machine learning supervisés. Ils sont basés sur une structure hiérarchique de questions (nœuds) et de réponses (feuilles) qui permettent de faire des prédictions à partir d'une variable cible. Les arbres de décision sont souvent utilisés pour résoudre des problèmes de classification binaire et multi-classes, ainsi que pour l'analyse de données de type régression. Les arbres de décision sont souvent très interprétables car ils permettent de visualiser les règles de décision prises par le modèle. Cependant, ils peuvent être sujets à surapprentissage lorsque la complexité du modèle est trop élevée."
    }
      
    model_selected = st.radio("", models, label_visibility="collapsed")
    st.write(":information_source:", model_descriptions[model_selected])
 
    st.markdown("""
---
Le jeu de données utilisé dans ce projet est une série temporelle multivariée, c'est-à-dire qu'il regroupe l'évolution temporelle de plusieurs variables explicatives. Cela permet la détection de corrélations entre ces variables au fil du temps. Pour gérer ce type de données, nous avons considéré différents modèles de séries temporelles multivariées. Ces modèles incluent des techniques de décomposition de séries temporelles pour isoler les tendances, les saisons et les résidus des séries.
""")

    ts_models = ["ARIMA (Auto-Regressive Integrated Moving Average)", 
         "SARIMA (Seasonal Auto-Regressive Integrated Moving Average)"]

    ts_model_descriptions = {
        "ARIMA (Auto-Regressive Integrated Moving Average)": 
        "Le modèle **ARIMA** (Auto-Regressive Integrated Moving Average) est un modèle statistique utilisé pour l'analyse et la prévision des séries chronologiques. Il combine des modèles d'autorégression (AR), de différenciation (I) et de moyenne mobile (MA) pour comprendre les tendances et saisonnalités dans les données. Il est souvent utilisé pour prévoir des événements tels que les ventes, les émissions de gaz à effet de serre, la consommation énergétique, etc.",
        "SARIMA (Seasonal Auto-Regressive Integrated Moving Average)":
        "Le modèle **SARIMA** (Seasonal Auto-Regressive Integrated Moving Average) est une extension de l'ARIMA qui prend en compte les tendances saisonnières dans les données. Il est utilisé pour les séries chronologiques avec des tendances saisonnières, comme les données de vente au détail, de tourisme, de météo, etc. C'est un outil efficace pour la détection des tendances saisonnières et l'analyse des tendances de fond dans les données."
    }
    
    ts_model_selected = st.radio("", ts_models, label_visibility="collapsed")
    st.write(":information_source:", ts_model_descriptions[ts_model_selected])
    
    st.subheader("Classification de données déséquilibrées")
    st.markdown("""
Ce projet se concentre sur la classification de données déséquilibrées, similaire à la détection d'anomalies. Pour traiter les données déséquilibrées, nous avons recours à des techniques de sous-échantillonnage et sur-échantillonnage pour rééquilibrer les données et sélectionner la méthode la plus efficace en fonction des métriques choisies. La technique du sous-échantillonnage "RandomUnderSampler" a été utilisée car elle s'est avérée la plus performante étant donné l'ampleur de notre ensemble de données (145,460 observations) et les conséquences sur les performances de certains algorithmes.
""")

    data = {'Classe 0 : 78%': 78, 'Classe 1 : 22%': 22}
    plt.pie(data.values(), labels=data.keys())

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    im1 = Image.open(buf)

    data = {
        "Ensemble d'entraînement": {'class 0': 76696, 'class 1': 21854},
        "Ensemble d'entraînement rééchantillonné": {'class 0': 21854, 'class 1': 21854},
        "Ensemble de test": {'class 0': 32890, 'class 1': 9347}
    }

    fig = go.Figure()
    colors = {"Ensemble d'entraînement": ['blue', 'blue'], "Ensemble d'entraînement rééchantillonné": ['purple', 'purple'],"Ensemble de test": ['orange', 'orange']}
    for name, value in data.items():
        fig.add_trace(go.Bar(x=list(value.keys()), y=list(value.values()), name=name, marker=dict(color=colors[name])))
    fig.update_layout(barmode='group')    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(im1, use_column_width='auto', caption="Répartition des classes de la variable cible \"RainTomorrow\"")
    with col2:
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Classification pénalisée")
    st.markdown("""
La classification pénalisée est une technique utilisée pour traiter les cas de données déséquilibrées. Elle permet d’appliquer des coûts supplémentaires au modèle pour les erreurs de classification commises sur la classe minoritaire pendant l'entraînement. Ces pénalités sur les erreurs ont pour objectif d'inciter les modèles à accorder plus d'attention à la classe minoritaire, afin de réduire les biais dans les prédictions.

Un des moyens courant pour mettre en place cette technique est d'utiliser l'argument "balanced" lors de la définition du modèle, ce qui permet d'attribuer à chaque classe un poids inversement proportionnel à sa fréquence d'apparition dans les données d'entraînement. Pour aller plus loin nous avons également testé différents ratios sur les classes pour déterminer la configuration qui donne les meilleurs résultats par rapport aux métriques principales et secondaires.

En complément, nous avons ajusté le seuil de probabilité à partir duquel les prédictions sont classées comme positives ou nulles, c'est-à-dire la valeur seuil à partir de laquelle un individu sera classé dans la classe majoritaire ou la classe minoritaire. Ajuster ce seuil de manière optimale nous permet de marquer plus distinctement les classes et d'améliorer les performances de notre modèle.
""")
    
    st.subheader("Métrique de performance principale")
    st.markdown("""
Lorsque l'on travaille sur un jeu de données de classification binaire déséquilibré, il est crucial d'utiliser des métriques de performance appropriées pour évaluer les performances de notre modèle. Pour évaluer les performances de ces modèles, des mesures de performance comme l'accuracy, le f1_score, la précision et le rappel ont été utilisées. Cependant, il est important de noter que ces mesures ne donnent pas une image complète de la performance du modèle car elles sont souvent biaisées en faveur de la classe majoritaire. C'est pourquoi il est important d'utiliser des métriques de performance secondaires pour obtenir une vision complète des performances de nos modèles. \n

Parmi les métriques de performance secondaires couramment utilisées pour les jeux de données déséquilibrés, la métrique **f1_macro** est particulièrement judicieuse en tant que métrique de performance principale. Cette métrique calcule la moyenne arithmétique du f1_score pour chaque classe, en traitant ainsi toutes les classes de la même manière, quelle que soit leur distribution. Cette métrique est particulièrement adaptée pour les situations de classes déséquilibrées, car elle est indépendante de la répartition des classes dans les données. En plus de donner une idée plus précise des performances de notre modèle en prenant en compte les erreurs de classification pour les classes minoritaires, elle permet également de mieux comprendre les performances de chaque classe spécifique, ce qui est crucial pour pouvoir identifier les lacunes de performance pour les classes minoritaires. 
""")

    metrics = ["f1_score", "f1_micro", "f1_weighted", "f1_macro"]
    metrics_descriptions = {
        "f1_score": 
        "Le **f1_score** est une métrique de performance couramment utilisée pour évaluer les modèles de classification. Il est calculé en prenant la moyenne harmonique entre la précision et le rappel. La précision est le taux de prédictions positives correctes, c'est-à-dire le nombre de vrais positifs divisé par le nombre total de prédictions positives. Le rappel est le taux de positifs correctement prédits, c'est-à-dire le nombre de vrais positifs divisé par le nombre total de vrais positifs et de faux négatifs.",
        "f1_micro":
        "Le **f1_micro** est une variante de la métrique f1_score qui calcule une seule valeur globale pour l'ensemble des données en tenant compte de toutes les observations, indépendamment de la classe à laquelle elles appartiennent. Il est calculé en utilisant les vrais positifs, les faux positifs et les faux négatifs totaux pour l'ensemble des classes, au lieu de les calculer séparément pour chaque classe et de les moyenner ensuite.",
        "f1_weighted": 
        "Le **f1_weighted** est une variante de la métrique f1_score qui prend en compte la répartition des classes dans les données. Il calcule la moyenne pondérée des f1_score pour chaque classe en utilisant le nombre d'exemples de chaque classe comme poids. Cela signifie que les classes avec plus d'exemples auront plus d'influence sur la valeur globale de la métrique.",
        "f1_macro":
        "Le **f1_macro** est une méthode d'évaluation pour les modèles de classification qui calcule la moyenne des f1_score pour chaque classe sans tenir compte de la répartition des classes dans les données."
    }    
    
    metrics_pros = {
        "f1_score": 
        """Les **avantages** incluent:
- sa capacité à combiner les deux métriques de précision et de rappel en une seule, ce qui permet une évaluation plus complète des performances d'un modèle de classification en tenant compte à la fois de la précision et du rappel.
- sa pertinence pour les jeux de données déséquilibrés, où les classes ne sont pas représentées de manière égale. En utilisant le f1_score, on peut avoir une idée de la qualité globale de la classification en tenant compte des performances des différentes classes.
- son utilité pour les problèmes de classification binaires, où la précision et le rappel sont des métriques importantes pour évaluer les performances.""",
        "f1_micro":
        """Les **avantages** incluent:
- sa capacité à donner une idée de la qualité globale de la classification en prenant en compte toutes les observations indépendamment de la classe à laquelle elles appartiennent.
- sa pertinence pour les jeux de données déséquilibrés, où la classe minoritaire est très petite et où la métrique f1_score peut être biaisée.
- sa capacité à prendre en compte toutes les observations, il est donc plus robuste à la présence de données déséquilibrées.""",
        "f1_weighted":
        """Les **avantages** incluent:
- sa capacité à tenir compte de la répartition des classes dans les données en utilisant le nombre d'exemples de chaque classe comme poids pour calculer la moyenne pondérée des f1_score pour chaque classe.
- sa pertinence pour les jeux de données où les classes ont des tailles très différentes, cette métrique permet de considérer les performances pour chaque classe spécifique.
- sa capacité à donner une idée de la qualité globale de la classification en prenant en compte les performances des différentes classes.""",
        "f1_macro":
        """Les **avantages** incluent:
- sa capacité à fournir une mesure de la performance moyenne pour chaque classe, ce qui est particulièrement utile lorsque les tailles des classes sont similaires.
- sa capacité à donner une idée générale de la performance globale des modèles de classification.
- sa capacité à être utilisée pour évaluer les performances de différents modèles de classification sur des jeux de données à classes multiples.
- sa capacité à être combinée avec d'autres métriques pour obtenir une vision complète de la performance des modèles.
- sa capacité à fournir une évaluation précise de la performance pour les classes minoritaires.
- sa capacité à prendre en compte les performances sur les classes minoritaires tout en tenant compte de la répartition des classes dans les données.
- sa capacité à être utilisée pour évaluer les performances de différents modèles de classification sur des jeux de données déséquilibrées.
        """
    }
    
    metrics_cons = {
        "f1_score": 
        """Les **inconvénients** incluent:
- sa sensibilité aux données déséquilibrées, c'est-à-dire lorsque les classes ne sont pas représentées de manière égale, cela peut affecter de manière significative la valeur du f1_score, cela peut rendre les résultats faux ou trompeurs.
- son manque d'indication sur les performances de chaque classe spécifique, en utilisant seulement le f1_score, il est difficile de savoir comment les classes individuelles sont classées. Il est donc important de combiner le f1_score avec d'autres métriques pour avoir une image complète des performances.
        """,
        "f1_micro":
        """Les **inconvénients** incluent:
- son manque d'indication sur les performances de chaque classe spécifique, en utilisant seulement le f1_micro, il est difficile de savoir comment les classes individuelles sont classées. Il est donc important de combiner le f1_micro avec d'autres métriques pour avoir une image complète des performances.
- sa sensibilité aux données déséquilibrées, c'est-à-dire lorsque les classes ne sont pas représentées de manière égale, cela peut affecter de manière significative la valeur du f1_micro, cela peut rendre les résultats faux ou trompeurs.
        """,
        "f1_weighted": 
        """Les **inconvénients** incluent:
- son risque de survaloriser les classes plus grandes si les performances pour les classes plus petites sont faibles, en utilisant le nombre d'exemples de chaque classe comme poids pour calculer la moyenne pondérée des f1_score pour chaque classe, les classes plus grandes auront plus d'influence sur la valeur globale de la métrique, ce qui peut donner une fausse image des performances si les performances pour les classes plus petites sont faibles.
- sa difficulté à comprendre et à interpréter les résultats, car les poids de chaque classe peuvent être difficiles à comprendre pour les utilisateurs non expérimentés.
        """,
        "f1_macro":
        """Les **inconvénients** incluent:
- sa tendance à sous-estimer la performance globale lorsque les tailles des classes sont très différentes.
- son manque de prise en compte de la répartition des classes dans les données.
- son incapacité à fournir une évaluation précise de la performance pour les classes minoritaires.
- sa capacité à donner des résultats trompeurs pour les jeux de données déséquilibrés.
        """
    }
    
    metrics_expressions = {
        "f1_score":
        """$\quad \\text{f1\_score} = 2 \\times \\frac{\\text{\\normalsize{precision}}\,\\times\,\\text{\\normalsize{recall}}}{\\text{\\normalsize{precision}}\,+\,\\text{\\normalsize{recall}}}
        = \\frac{\\text{\\normalsize{TP}}}{\\text{\\normalsize{TP}}\,+\,\\text{\\normalsize{1/2}}\,\\times\,\\text{\\normalsize{(FN\,+\,FP)}}}$""",
        "f1_micro":
        """$\quad \\text{f1\_micro} = \\text{\\normalsize{accuracy = precision\_micro = recall\_micro}}
        = \\frac{\\text{\\normalsize{TP}}}{\\text{\\normalsize{TP}}\,+\,\\text{\\normalsize{1/2}}\,\\times\,\\text{\\normalsize{(FN\,+\,FP)}}}$""",
        "f1_weighted":
        "$\quad \\text{f1\_weighted} = 2 \\times \\frac{\sum_{i=1}^{n} \\text{\\normalsize{w\_i}} \,\\times\, \\text{\\normalsize{precision\_i}} \,\\times\, \\text{\\normalsize{recall\_i}}}{\sum_{i=1}^{n} \\text{\\normalsize{w\_i}} \,\\times\, (\\text{\\normalsize{precision\_i}} \,+\, \\text{\\normalsize{recall\_i}})}$",
        "f1_macro":
        "$\quad \\text{f1\_macro} = \\frac{\\sum_{i=1}^n \\text{\\normalsize{f1\_score\_i}}}{\\text{\\normalsize{n}}}$",
    }
    
    metric_selected = st.radio("", metrics, label_visibility="collapsed")
    st.write(":information_source:", metrics_descriptions[metric_selected])
    st.write(":heavy_plus_sign:", metrics_pros[metric_selected])
    st.write(":heavy_minus_sign:", metrics_cons[metric_selected])
    st.write(":pencil2:", metrics_expressions[metric_selected])
    
    st.subheader("Métriques de performance secondaires")
    st.markdown("""Dans le cadre de la modélisation d'un problème de classification binaire sur jeu de données déséquilibré, il est crucial d'utiliser des métriques de performance secondaires pour évaluer les performances de notre modèle. La métrique de performance f1_macro est couramment utilisée pour les jeux de données déséquilibrées car elle calcule la moyenne arithmétique du f1_score pour chaque classe, indépendamment de leur distribution. Cependant, elle ne donne pas d'indication sur les performances de chaque classe spécifique et peut sous-estimer les performances globales si certaines classes ont des tailles très différentes. Il est donc important de la combiner avec d'autres métriques pour avoir une analyse plus complète des performances du modèle.
""")
    
    sec_metrics = ["balanced_accuracy", "geometric_mean", "roc_auc"]
    sec_metrics_descriptions = {
        "balanced_accuracy":
        """ La **balanced accuracy** est une méthode d'évaluation de la performance des modèles de classification qui prend en compte la répartition des classes dans les données en calculant la moyenne arithmétique de la sensibilité et de la spécificité pour chaque classe. Cela permet d'évaluer la performance du modèle de manière plus équilibrée et de prendre en compte les performances de chaque classe, indépendamment de leur répartition dans les données. Elle est particulièrement adaptée pour les jeux de données déséquilibrés et permet une meilleure prise en compte des classes minoritaires pour une évaluation plus précise de la performance du modèle.""",
        "geometric_mean":
        """La **geometric_mean** est une approche pour évaluer les performances d'un modèle de classification en tenant compte de la répartition des classes dans les données. Elle calcule généralement la racine carrée du produit des sensibilités pour chaque classe. Cette méthode est particulièrement utile pour les jeux de données déséquilibrés, car elle permet de maximiser la précision pour chaque classe tout en maintenant un équilibre entre les performances de chaque classe. Elle est souvent utilisée en conjonction avec d'autres métriques pour évaluer les performances de modèles de classification multi-classes.
Pour la classification binaire, elle est également la racine carrée du produit de la sensibilité et de la spécificité.""",
        "roc_auc": 
        """La métrique **roc_auc** (Receiver Operating Characteristic - Area Under the Curve) est utilisée pour évaluer les modèles de classification binaire en prenant en compte le compromis entre les taux de vrais positifs et les taux de faux positifs pour un modèle donné. Elle utilise la courbe ROC qui représente les taux de vrais positifs en fonction des taux de faux positifs pour visualiser les performances d'un modèle pour différents seuils de classification. L'AUC (Area Under the Curve) est ensuite utilisée pour quantifier ces performances en un seul score numérique. Cette métrique est particulièrement utile pour les jeux de données déséquilibrées car elle prend en compte la distribution des classes dans les données et permet de mieux comprendre les performances d'un modèle en termes de capacité à détecter les cas positifs. Il est en effet important de noter qu'elle peut être sensible aux données déséquilibrées, car un petit nombre de prédictions correctes/incorrectes peut entraîner une grande variation du score."""
    }
    
    sec_metrics_pros = {
    "balanced_accuracy": 
    """Les **avantages** incluent:
- son adaptation aux jeux de données déséquilibrés, en prenant en compte la répartition des classes dans les données.
- sa capacité à donner une idée de la qualité globale de la classification en évaluant la performance moyenne pour chaque classe.
- sa capacité à évaluer les performances de chaque classe de manière indépendante de leur répartition dans les données.
    """,
    "geometric_mean":
    """Les **avantages** incluent:
- son adaptation aux jeux de données déséquilibrés.
- sa capacité à maximiser les performances pour chaque classe tout en maintenant un équilibre entre les performances des différentes classes.
- sa capacité à donner une vision équilibrée des performances pour chaque classe.
- sa capacité à donner une idée de la qualité globale de la classification.
- sa capacité à être utilisée pour évaluer les performances des modèles sur les classes minoritaires.
- sa capacité à être utilisée pour évaluer les performances de différents modèles de classification sur des jeux de données déséquilibrées.
    """,
    "roc_auc":
    """Les **avantages** incluent:
- son indépendance vis-à-vis du seuil de classification, permettant de mieux comprendre les performances d'un modèle en termes de capacité à détecter les cas positifs.
- sa capacité à donner une idée de la performance globale d'un modèle.
- sa pertinence pour les jeux de données déséquilibrés en raison de sa capacité à prendre en compte la distribution des classes dans les données.
    """
    }
    
    sec_metrics_cons = {
    "balanced_accuracy": 
    """Les **inconvénients** incluent:
- son interprétation peut être difficile pour certains utilisateurs qui sont plus familiers avec des métriques plus courantes comme l'accuracy.
- son utilisation peut être biaisée dans des cas où l'on souhaite maximiser l'accuracy pour une classe spécifique.
- son utilisation peut être inappropriée dans des cas où les classes ont des tailles très différentes.
- sa moindre robustesse que d'autres métriques en cas de données extrêmement déséquilibrées.
    """,
    "geometric_mean":
    """Les **inconvénients** incluent:
- sa sensibilité aux données déséquilibrées, où un petit nombre de prédictions correctes/incorrectes peut entraîner une grande variation du score.
- son incapacité à être adaptée à tous les types de données, il est donc important de combiner son utilisation avec d'autres métriques de performance pour obtenir une vision complète des performances du modèle.
- sa difficulté à être interprétée pour certains utilisateurs qui sont plus familiers avec des métriques plus courantes comme l'accuracy.
- son incapacité à évaluer correctement les performances des modèles dans les cas où certaines classes ont des tailles très différentes.
- sa moindre robustesse que d'autres métriques en cas de données extrêmement déséquilibrées.
    """,
    "roc_auc":
    """Les **inconvénients** de la métrique ROC-AUC incluent :
- son incapacité à donner une indication sur les performances de chaque classe spécifique.
- sa sensibilité aux variations de la distribution des données, qui peut entraîner une surévaluation des performances dans les cas où les données sont déséquilibrées.
- son incapacité à prendre en compte les coûts associés aux erreurs de classification, c'est-à-dire les conséquences de classer un exemple de classe A en tant qu'exemple de classe B.
- son incapacité à être facilement interprétée pour les utilisateurs qui ne sont pas familiers avec les courbes ROC.
- sa sensibilité aux variations des seuils de classification, nécessitant un choix judicieux de ces derniers.
    """
    }
    
    sec_metrics_expressions = {
        "balanced_accuracy":
        "$\quad \\text{balanced\_accuracy} = \\frac{\\text{\\normalsize{sensibilité}} \,+\, \\text{\\normalsize{spécificité}}}{\\text{\\normalsize{2}}}$",
        "geometric_mean":
        "$\quad \\text{geometric\_mean} = \sqrt{\prod_{i=1}^{n} \\text{\\normalsize{sensibilité\_i}}}$",
        "roc_auc":
        "$\quad \\text{roc\_auc} =  \sum_{i}^{n} (\\text{\\normalsize{sensibilité\_i}} - \\text{\\normalsize{sensibilité\_{i-1}}}) \\times (\\text{\\normalsize{1 - spécificité\_i}})$"
    }
    
    sec_metric_selected = st.radio("", sec_metrics, label_visibility="collapsed")
    st.write(":information_source:", sec_metrics_descriptions[sec_metric_selected])
    st.write(":heavy_plus_sign:", sec_metrics_pros[sec_metric_selected])
    st.write(":heavy_minus_sign:", sec_metrics_cons[sec_metric_selected])
    st.write(":pencil2:", sec_metrics_expressions[sec_metric_selected])
    
    st.header("Evaluation des modèles prédictifs")
    st.subheader("Etude comparative")
    st.markdown("""
Une analyse comparative de différents modèles de classification binaire par apprentissage supervisé a été menée en utilisant des métriques d'évaluation adaptées aux jeux de données déséquilibrés. Les modèles ont été comparés avec et sans méthode de rééchantillonnage. Les performances des métriques choisies ont été évaluées en sélectionnant les meilleurs estimateurs à partir d'une grille de paramètres. Les résultats ont été consolidés par validation croisée et illustrés par des courbes ROC, de gain cumulé et de précision-rappel. Une analyse basée sur la pondération des classes a été effectuée pour tous les modèles, à l'exception de KNN, et le seuil de probabilité a été ajusté pour une meilleure distinction des classes. \n

Les meilleures performances de prévision de précipitations ont été obtenues avec une étape de sous-échantillonnage. Les performances de différents algorithmes sont résumées dans le tableau ci-dessous:
""")
    
    df_scores = pd.DataFrame(data=[[0.599413, 0.719396, 0.772318, 0.772312, 0.772318],
                                   [0.599413, 0.719396, 0.772318, 0.772312, 0.772318],
                                   [0.599388, 0.719374, 0.772302, 0.772297, 0.772302],
                                   [0.621623, 0.736925, 0.787982, 0.787981, 0.787982],
                                   [0.622077, 0.736842, 0.788919, 0.788911, 0.788919],
                                   [0.621099, 0.736475, 0.787678, 0.787677, 0.787678],
                                   [0.612058, 0.729644, 0.781015, 0.781014, 0.781015],
                                   [0.611697, 0.729226, 0.780933, 0.780932, 0.780933],
                                   [0.616739, 0.732989, 0.784738, 0.784736, 0.784738],
                                   [0.605684, 0.720882, 0.781044, 0.780715, 0.781044],
                                   [0.585779, 0.708628, 0.762235, 0.762228, 0.762235],
                                   [0.585861, 0.708685, 0.762304, 0.762297, 0.762304],
                                   [0.578797, 0.697870, 0.761813, 0.761201, 0.761813]], 
                             columns=['f1_score', 'f1_macro', 'bal_acc', 'moy_geom', 'roc_auc'], 
                             index=['lr1', 'lr2', 'lr3', 'rf0', 'rf1', 'rf2', 'svm0', 'svm1', 'svm2', 'knn', 'dt0', 'dt1', 'dt2'])

    tab1, tab2, tab3 = st.tabs(["Tableau", "Graphique", "Histogramme"])
    
    with tab1:
        st.dataframe(df_scores.style.highlight_max(axis=0), use_container_width=True)
    
    with tab2:
        st.line_chart(df_scores, x=['f1_score', 'f1_macro', 'bal_acc', 'moy_geom', 'roc_auc'], use_container_width=True)
    
    with tab3:
        st.bar_chart(df_scores, x=['f1_score', 'f1_macro', 'bal_acc', 'moy_geom', 'roc_auc'], use_container_width=True)
    
    st.warning("""
Pour chaque algorithme considéré (à l'exception du modèle KNN), les index 1, 2 et 3 représentent les différentes itérations d'une étude comparative basée sur la pondération des classes. Ces itérations consistent à utiliser différents paramètres de pondération des classes dans la définition du modèle :

- Itération 1 : "class_weight = None"
- Itération 2 : "class_weight = 'balanced'"
- Itération 3 : "class_weight = {0: x, 1: 1-x}"

En outre, pour améliorer la distinction entre les classes, un seuil de probabilité est adapté automatiquement pour tous les modèles. Cela permet de classer les prédictions comme positives ou nulles de manière plus précise.    
""", icon="⚠️")
    
    st.subheader("Choix du meilleur modèle")
    st.markdown("Les meilleures performances des modèles étudiés sont résumées ci-dessous :")
    
    df_best_scores = pd.DataFrame(data=[[0.599413, 0.719396, 0.772318, 0.772312, 0.772318],
                                        [0.622077, 0.736842, 0.788919, 0.788911, 0.788919],
                                        [0.616739, 0.732989, 0.784738, 0.784736, 0.784738],
                                        [0.605684, 0.720882, 0.781044, 0.780715, 0.781044],
                                        [0.585861, 0.708685, 0.762304, 0.762297, 0.762304]], 
                             columns=['f1_score', 'f1_macro', 'bal_acc', 'moy_geom', 'roc_auc'], 
                             index=['lr', 'rf', 'svm', 'knn', 'dt'])
        
    tab1, tab2, tab3 = st.tabs(["Tableau", "Graphique", "Histogramme"])
    
    with tab1:
        st.dataframe(df_best_scores.style.highlight_max(axis=0), use_container_width=True)  
    
    with tab2:
        st.line_chart(df_best_scores, x=['f1_score', 'f1_macro', 'bal_acc', 'moy_geom', 'roc_auc'], use_container_width=True)
    
    with tab3:
        st.bar_chart(df_best_scores, x=['f1_score', 'f1_macro', 'bal_acc', 'moy_geom', 'roc_auc'], use_container_width=True)
    
    st.markdown("""
Après avoir entraîné plusieurs modèles sur des features sélectionnées à partir de jeux de données nettoyés, nous avons opté pour un modèle de **forêt aléatoire** en raison de ses performances remarquables sur les métriques choisies. En termes pratiques, le temps de calcul et les ressources matérielles requises pour ce modèle étaient moins élevés que pour l'autre modèle le plus proche, SVM. Cette caractéristique rendait la forêt aléatoire plus facile à gérer pour des calculs locaux ou pour les services Cloud gratuits. De plus, la capacité d'interprétation des résultats obtenus avec la forêt aléatoire s'est avérée supérieure à celle de SVM.

Bien que des traces de sur-entraînement (légère différence de score entre le jeu d'entraînement et le jeu de test) ont été repérées, les résultats de la validation croisée ont démontré que l'erreur sur le score du jeu de données était minime, il n'est donc pas nécessaire de poursuivre les analyses.
    """)
    

    

    