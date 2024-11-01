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
    st.markdown("""<style>.normal-font {font-size:13.5pt}</style>""", unsafe_allow_html=True)
    st.markdown("""<style>.small-font {font-size:11.5pt}</style>""", unsafe_allow_html=True)
    st.markdown("""<p class="normal-font">
Ce projet vise à résoudre un problème de <b>classification binaire</b> en utilisant des techniques d'<b>apprentissage supervisé</b>. Il s'agit de prévoir la valeur d'une variable cible quantitative en utilisant des données étiquetées qui comprennent des entrées et des sorties. Grâce à ces étiquettes, le modèle peut évaluer son exactitude et continuer à s'améliorer au fil du temps. En utilisant des techniques d'apprentissage supervisé, le modèle est capable de généraliser à de nouvelles données, en s'appuyant sur les connaissances acquises lors de l'entraînement.</p>

<p class="normal-font">Nous avons testé différents modèles de classification binaire pour prédire une variable cible et déterminer le meilleur modèle pour résoudre notre problème de classification binaire en comparant les algorithmes utilisés.
</p>""", unsafe_allow_html=True)
    
    models = ["Régression logistique (Logistic Regression)", 
          "Forêts aléatoires (Random Forest)", 
          "Séparateurs à vaste marge (Support Vector Machine)", 
          "K-plus proches voisins (K-Nearest Neighbors)", 
          "Arbres de décision (Decision Tree)"]

    model_descriptions = {
        "Régression logistique (Logistic Regression)": 
        "_La **régression logistique** est un modèle statistique utilisé pour résoudre des problèmes de classification binaire ou multi-classes en prédisant la probabilité d'appartenance à une classe donnée en fonction d'un ensemble de variables explicatives. Elle utilise une fonction logistique pour modéliser la probabilité de l'événement cible en fonction des variables indépendantes. Elle permet de maximiser la vraisemblance des données pour obtenir les coefficients de régression les plus probables et de les utiliser pour faire des prédictions sur de nouvelles observations. Cette méthode est souvent utilisée pour la classification binaire car elle permet de gérer les cas où les classes sont déséquilibrées._",
        "Forêts aléatoires (Random Forest)":
        "_Les **forêts aléatoires** sont un ensemble de modèles de décision basés sur des arbres de décision qui utilisent une technique d'échantillonnage aléatoire pour construire de nombreux arbres de décision et ensuite combiner leurs prédictions. Cette combinaison permet de réduire la variance des prédictions individuelles des arbres et d'améliorer la robustesse et la performance globale du modèle. Les forêts aléatoires peuvent être utilisées pour la classification et la régression, et sont particulièrement utiles pour les jeux de données complexes et les problèmes de surapprentissage. Ils offrent également la possibilité de mesurer l'importance relative des variables, permettant une meilleure interprétabilité des résultats._",
        "Séparateurs à vaste marge (Support Vector Machine)":
        "_Les **séparateurs à vastes marges** sont une classe de modèles de classification supervisée qui cherchent à maximiser la marge, c'est-à-dire la distance entre les points de données les plus proches des frontières de décision, pour séparer les classes. Ils utilisent un noyau, une fonction qui permet de projeter les données dans un espace de plus grande dimension, pour rendre les classes séparable par un hyperplan. Les séparateurs à vastes marges sont souvent utilisés pour la reconnaissance de formes et les tâches de reconnaissance d'images en raison de leur capacité à gérer efficacement les données non linéaires._",
        "K-plus proches voisins (K-Nearest Neighbors)":
        "_Les **K-plus proches voisins** sont un type d'algorithme de classification basé sur l'apprentissage non supervisé utilisant une méthode de \"voisinage\" pour classer les nouvelles observations. Il consiste à définir un nombre fixe de voisins (K) et à classer une nouvelle observation en fonction de la majorité des classes de ses K plus proches voisins dans l'ensemble de données d'entraînement. Il est simple à implémenter et peut s'adapter à des données non linéaires, mais peut être sujet à des erreurs de classification en cas de données bruyantes ou déséquilibrées._",
        "Arbres de décision (Decision Tree)":
        "_Les **arbres de décision** sont un type de modèle de classification supervisé utilisé pour prédire la classe d'un objet en se basant sur les valeurs de ses caractéristiques. Ils utilisent une structure hiérarchique de décisions basée sur des tests conditionnels pour diviser les données en sous-ensembles plus petits jusqu'à ce qu'ils atteignent des feuilles qui prédisent une classe. Les arbres de décision peuvent également être utilisés pour la régression en utilisant des valeurs continues plutôt que des étiquettes de classe. Ils sont souvent utilisés pour leur simplicité d'utilisation et leur capacité à gérer des données catégorielles et numériques._"
    }
      
    model_selected = st.radio("", models, label_visibility="collapsed")
    st.write(":information_source:", model_descriptions[model_selected])
 
    st.markdown("""
<p class="normal-font">Le jeu de données utilisé dans ce projet est une <b>série temporelle multivariée</b>, c'est-à-dire qu'il regroupe l'évolution temporelle de plusieurs variables explicatives. Cela permet la détection de corrélations entre ces variables au fil du temps. Pour gérer ce type de données, nous avons également considéré différents modèles de séries temporelles multivariées. Ces modèles incluent des techniques de décomposition de séries temporelles pour isoler les tendances, les saisons et les résidus des séries.</p>
""", unsafe_allow_html=True)

    ts_models = ["ARIMA (Auto-Regressive Integrated Moving Average)", 
         "SARIMA (Seasonal Auto-Regressive Integrated Moving Average)"]

    ts_model_descriptions = {
        "ARIMA (Auto-Regressive Integrated Moving Average)": 
        "_Le modèle **ARIMA** est un modèle statistique utilisé pour la prédiction de séries chronologiques. Il combine les concepts des modèles auto-régressifs (AR) et des modèles de moyenne mobile (MA) pour capturer les tendances et les saisons d'une série chronologique. L'intégration (I) permet également de prendre en compte les effets d'une série chronologique non stationnaire en la différenciant une ou plusieurs fois pour obtenir une série stationnaire. L'ARIMA peut être utilisé pour identifier les tendances cachées, les saisons, les cycles et les erreurs aléatoires dans les données chronologiques, et pour fournir des prévisions fiables._",
        "SARIMA (Seasonal Auto-Regressive Integrated Moving Average)":
        "_Le modèle **SARIMA** est un modèle statistique utilisé pour la prévision de séries chronologiques temporelles. Il combine les caractéristiques des modèles ARIMA et des modèles de saisonnalité en incluant des termes de saisonnalité dans les paramètres de régression auto-régressive et de moyenne mobile. Il est utilisé pour capturer les tendances saisonnières et les corrélations à court et à long terme dans les données._"
    }
    
    ts_model_selected = st.radio("", ts_models, label_visibility="collapsed")
    st.write(":information_source:", ts_model_descriptions[ts_model_selected])
    
    st.subheader("Classification de données déséquilibrées")
    st.markdown("""
<p class="normal-font">Ce projet se concentre sur la <b>classification de données déséquilibrées</b>, similaire à la détection d'anomalies. Pour traiter les données déséquilibrées, nous avons recours à des techniques de sous-échantillonnage et sur-échantillonnage pour rééquilibrer les données et sélectionner la méthode la plus efficace en fonction des métriques choisies. La technique du sous-échantillonnage <em>"RandomUnderSampler"</em> a été utilisée car elle s'est avérée la plus performante étant donné l'ampleur de notre ensemble de données (145,460 observations) et les conséquences sur les performances de certains algorithmes.</p>
""", unsafe_allow_html=True)

    data = {'Classe 0 : 78%': 78, 'Classe 1 : 22%': 22}
    plt.pie(data.values(), labels=data.keys())
    plt.title("Répartition des classes de la variable cible \"RainTomorrow\"", fontsize=13.5, fontweight="bold")

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
    colors = {"Ensemble d'entraînement": ['blue', 'blue'], "Ensemble d'entraînement rééchantillonné": ['purple', 'purple'], "Ensemble de test": ['orange', 'orange']}
    for name, value in data.items():
        fig.add_trace(go.Bar(x=list(value.keys()), y=list(value.values()), name=name, marker=dict(color=colors[name])))
    fig.update_layout(barmode='group', yaxis_title='Taille du jeu de données',width=500,height=700)    
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(im1, use_column_width='auto')
    with col2:
        st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Classification pénalisée")
    st.markdown("""
<p class="normal-font">La <b>classification pénalisée</b> est une technique utilisée pour traiter les cas de données déséquilibrées. Elle permet d’appliquer des coûts supplémentaires au modèle pour les erreurs de classification commises sur la classe minoritaire pendant l'entraînement. Ces pénalités sur les erreurs ont pour objectif d'inciter les modèles à accorder plus d'attention à la classe minoritaire, afin de réduire les biais dans les prédictions.</p>

<p class="normal-font">Un des moyens courant pour mettre en place cette technique est d'utiliser l'argument <em>"class_weight = 'balanced'"</em> lors de la définition du modèle, ce qui permet d'attribuer à chaque classe un poids inversement proportionnel à sa fréquence d'apparition dans les données d'entraînement. Pour aller plus loin, nous avons également testé différents ratios sur les classes en utilisant <em>"class_weight = {0: x, 1: 1-x}"</em> pour déterminer la configuration qui donne les meilleurs résultats par rapport aux métriques principales et secondaires.</p>

<p class="normal-font">En complément, nous avons ajusté le seuil de probabilité à partir duquel les prédictions sont classées comme positives ou nulles, c'est-à-dire la valeur seuil à partir de laquelle un individu sera classé dans la classe majoritaire ou la classe minoritaire. Ajuster ce seuil de manière optimale nous permet de marquer plus distinctement les classes et d'améliorer les performances de notre modèle.</p>
""", unsafe_allow_html=True)
    
    st.subheader("Métrique de performance principale")
    st.markdown("""
<p class="normal-font">Lorsque l'on travaille sur un jeu de données de classification binaire déséquilibré, il est crucial d'utiliser des métriques de performance appropriées pour évaluer les performances de notre modèle. Pour évaluer les performances de ces modèles, des mesures de performance comme l'<em>accuracy</em>, le <em>f1_score</em>, la <em>précision</em> et le <em>rappel</em> ont été utilisées. Cependant, il est important de noter que ces mesures peuvent ne pas donner une image complète de la performance du modèle car elles peuvent être biaisées en faveur de la classe majoritaire. Il est donc important d'utiliser des métriques complémentaires pour obtenir une vision plus complète des performances de nos modèles.</p>

<p class="normal-font">Nous avons choisi la métrique <b>f1_macro</b> comme métrique de performance principale car elle est particulièrement adaptée pour les situations de classes déséquilibrées.</p>
""", unsafe_allow_html=True)

    metrics = ["f1_score", "f1_micro", "f1_weighted", "f1_macro"]
    metrics_descriptions = {
        "f1_score": 
        "_Le **f1_score** est une métrique d'évaluation pour les modèles de classification qui combine les informations de la précision (proportion de vrais positifs parmi tous les positifs prédits) et du rappel (proportion de vrais positifs parmi tous les vrais positifs) en un seul score._",
        "f1_micro":
        "_Le **f1_micro** est une variante de la métrique f1_score qui calcule une seule valeur globale pour l'ensemble des données en tenant compte de toutes les observations, indépendamment de la classe à laquelle elles appartiennent. Il est calculé en utilisant les vrais positifs, les faux positifs et les faux négatifs totaux pour l'ensemble des classes, au lieu de les calculer séparément pour chaque classe et de les moyenner ensuite._",
        "f1_weighted": 
        "_Le **f1_weighted** est une variante de la métrique f1_score qui prend en compte la répartition des classes dans les données. Il calcule la moyenne pondérée des f1_score pour chaque classe en utilisant le nombre d'exemples de chaque classe comme poids. Cela signifie que les classes avec plus d'exemples auront plus d'influence sur la valeur globale de la métrique._",
        "f1_macro":
        "_Le **f1_macro** est une méthode d'évaluation pour les modèles de classification qui calcule la moyenne arithmétique du f1_score pour chaque classe, en traitant ainsi toutes les classes de manière égale, indépendamment de leur fréquence dans les données._"
    }    
    
    metrics_pros = {
        "f1_score": 
        """:green[**Avantage majeur**]
- _Le **f1_score** prend en compte à la fois la précision et le rappel, ce qui permet de mesurer la performance de la classification en tenant compte de deux aspects importants : le nombre de vrais positifs et le nombre de faux positifs. Il est particulièrement utile pour les jeux de données déséquilibrés, où il est important de maximiser les performances pour les classes minoritaires._
    """,
        "f1_micro":
        """:green[**Avantage majeur**]
- _Le **f1_micro** prend en compte la performance globale pour toutes les classes, indépendamment de leur répartition dans les données. Il est particulièrement utile pour les jeux de données déséquilibrés, où il est important de maximiser les performances pour les classes minoritaires._
    """,
        "f1_weighted":
        """:green[**Avantage majeur**]
- _Le **f1_weighted** prend en compte la performance globale pour toutes les classes, tout en tenant compte des poids des classes pour améliorer la performance pour les classes minoritaires. Il est particulièrement utile pour les jeux de données déséquilibrés, où il est important de maximiser les performances pour les classes minoritaires._
    """,
        "f1_macro":
        """:green[**Avantage majeur**]
- _Le **f1_macro** prend en compte les performances pour chaque classe individuellement, ce qui est utile pour les jeux de données déséquilibrés. Il permet de mesurer la performance de la classification pour chaque classe indépendamment de leur répartition dans les données._
    """
    }
    
    metrics_cons = {
        "f1_score": 
        """:red[**Inconvénient majeur**]
- _Le **f1_score** est influencé par la répartition des classes dans les données, il peut donc sous-estimer la performance pour les classes minoritaires si la précision est faible. Il ne prend également pas en compte les performances pour chaque classe individuellement._
        """,
        "f1_micro":
        """:red[**Inconvénient majeur**]
- _Le **f1_micro** est influencé par la répartition des classes dans les données, il peut donc sous-estimer la performance pour les classes minoritaires si la précision est faible. Il ne prend également pas en compte les performances pour chaque classe individuellement._
        """,
        "f1_weighted": 
        """:red[**Inconvénient majeur**]
- _Le **f1_weighted** est influencé par la répartition des classes dans les données, il peut donc sous-estimer la performance pour les classes minoritaires si la précision est faible. Il ne prend également pas en compte les performances pour chaque classe individuellement._
        """,
        "f1_macro":
        """:red[**Inconvénient majeur**]
- _Le **f1_macro** ne tient pas compte de la répartition des classes dans les données, il peut donc sous-estimer la performance pour les classes minoritaires si la précision est faible._
    """
    }
    
    metrics_expressions = {
        "f1_score":
        """$\; \\text{f1\_score} = \\displaystyle{2 * \\frac{\\text{\\normalsize{précision}}*\\text{\\normalsize{rappel}}}{\\text{\\normalsize{précision}}+\\text{\\normalsize{rappel}}}}$""",
        "f1_micro":
        """$\; \\text{f1\_micro} = \\text{\\normalsize{accuracy = précision\_micro = rappel\_micro}}$""",
        "f1_weighted":
        "$\; \\text{f1\_weighted} = \\displaystyle{2 * \\frac{\\sum_{i=1}^{n} \\text{\\normalsize{w}}_i * \\text{\\normalsize{précision}}_i * \\text{\\normalsize{rappel}}_i}{\sum_{i=1}^{n} \\text{\\normalsize{w}}_i * (\\text{\\normalsize{précision}}_i + \\text{\\normalsize{rappel}}_i)}}$",
        "f1_macro":
        "$\; \\text{f1\_macro} = \\displaystyle{\\frac{\\sum_{i=1}^n \\text{\\normalsize{f1\_score}}_i}{\\text{\\normalsize{n}}}}$",
    }
    
    metric_selected = st.radio("", metrics, label_visibility="collapsed")
    st.write(":information_source:", metrics_descriptions[metric_selected])
    st.write(":heavy_plus_sign:", metrics_pros[metric_selected])
    st.write(":heavy_minus_sign:", metrics_cons[metric_selected])
    st.write(":pencil2:", metrics_expressions[metric_selected])
    
    st.subheader("Métriques de performance secondaires")
    st.markdown("""<p class="normal-font">Il est important d'utiliser des métriques de performances secondaires pour avoir une vue complète des performances d'un modèle de classification binaire. En utilisant une seule métrique, il est possible de sous-estimer les performances globales ou de ne pas avoir une vue précise des performances pour chaque classe spécifique. En utilisant des métriques supplémentaires, il est possible de combler les lacunes de la métrique principale et de mieux comprendre les performances du modèle, notamment pour les classes minoritaires. Cela permet également de choisir la métrique la plus adaptée pour le jeu de données spécifique et de prendre des décisions éclairées quant aux performances et à l'optimisation du modèle.</p>
""", unsafe_allow_html=True)
    
    sec_metrics = ["balanced_accuracy", "geometric_mean", "roc_auc"]
    sec_metrics_descriptions = {
        "balanced_accuracy":
        """_La **balanced_accuracy** est une méthode d'évaluation des modèles de classification binaire qui calcule la moyenne arithmétique des taux de vrais positifs et de vrais négatifs pour chaque classe en prenant en compte la répartition des classes dans les données. Cette métrique est particulièrement adaptée pour les situations de classes déséquilibrées car elle permet de tenir compte de la répartition des classes dans les données et de fournir une mesure de la performance pour chaque classe, indépendamment de la fréquence d'apparition de cette classe dans les données. Elle permet également de mieux comprendre les performances de chaque classe spécifique, ce qui est crucial pour pouvoir identifier les lacunes de performance pour les classes minoritaires._
        """,
        "geometric_mean":
        """_La **geometric_mean** est une méthode d'évaluation pour les modèles de classification binaire qui calcule la moyenne géométrique des taux de vrais positifs (TPR) et de vrais négatifs (TNR) pour chaque classe. Cette métrique est particulièrement utile pour les jeux de données déséquilibrées car elle permet de prendre en compte les performances des deux classes simultanément et de mettre l'accent sur les performances pour les classes minoritaires._
        """,
        "roc_auc": 
        """_La **roc_auc** est une méthode d'évaluation des modèles de classification binaire qui prend en compte le compromis entre les taux de vrais positifs et les taux de faux positifs pour un modèle donné. Elle utilise la courbe ROC qui représente les taux de vrais positifs en fonction des taux de faux positifs pour visualiser les performances d'un modèle pour différents seuils de classification. L'AUC (Area Under the Curve) est ensuite utilisée pour quantifier ces performances en un seul score numérique. Cette métrique est particulièrement utile pour les jeux de données déséquilibrées car elle prend en compte la distribution des classes dans les données et permet de mieux comprendre les performances d'un modèle en termes de capacité à détecter les cas positifs._
        """
    }
    
    sec_metrics_pros = {
    "balanced_accuracy": 
    """:green[**Avantage majeur**]
- _La **balanced accuracy** prend en compte la performance pour toutes les classes, tout en tenant compte des poids des classes pour améliorer la performance pour les classes minoritaires. Il est particulièrement utile pour les jeux de données déséquilibrés, où il est important de maximiser les performances pour les classes minoritaires._
    """,
    "geometric_mean":
    """:green[**Avantage majeur**]
- _La **moyenne géométrique** prend en compte la performance pour toutes les classes, tout en tenant compte des poids des classes pour améliorer la performance pour les classes minoritaires. Il est particulièrement utile pour les jeux de données déséquilibrés, où il est important de maximiser les performances pour les classes minoritaires._
    """,
    "roc_auc":
    """:green[**Avantage majeur**]
- _La **roc_auc** prend en compte tous les seuils de classification, ce qui est utile pour les jeux de données déséquilibrés. Il est insensible aux changements de seuil de classification, ce qui permet de mesurer la performance de la classification indépendamment du seuil choisi._
    """
    }
    
    sec_metrics_cons = {
    "balanced_accuracy": 
    """:red[**Inconvénient majeur**]
- _La **balanced accuracy** ne prend pas en compte la précision et le rappel de manière indépendante, elle peut donc sous-estimer la performance pour les classes minoritaires si la précision est faible. Elle peut également être influencée par les classes qui ont un grand nombre d'exemples._
    """,
    "geometric_mean":
    """:red[**Inconvénient majeur**]
- _La **moyenne géométrique** ne prend pas en compte la précision et le rappel de manière indépendante, elle peut donc sous-estimer la performance pour les classes minoritaires si la précision est faible. Elle peut également être influencée par les classes qui ont un grand nombre d'exemples._
    """,
    "roc_auc":
    """:red[**Inconvénient majeur**]
- _La **roc_auc** ne tient pas compte de la répartition des classes dans les données, il peut donc sous-estimer la performance pour les classes minoritaires si la précision est faible._
    """
    }
    
    sec_metrics_expressions = {
        "balanced_accuracy":
        "$\; \\text{balanced\_accuracy} = \\displaystyle{\\frac{\\text{\\normalsize{sensibilité}} + \\text{\\normalsize{spécificité}}}{\\text{\\normalsize{2}}}}$",
        "geometric_mean":
        "$\; \\text{geometric\_mean} = \\displaystyle{(\prod_{i=1}^{n} (TPR_i * TNR_i))^{\\frac{1}{n}}}$",
        "roc_auc":
        "$\; \\text{roc\_auc} =  \\displaystyle{\sum_{i}^{n} (\\text{\\normalsize{sensibilité}}_i - \\text{\\normalsize{sensibilité}}_{i-1}) * (\\text{\\normalsize{1 - spécificité}}_i)}$"
    }
    
    sec_metric_selected = st.radio("", sec_metrics, label_visibility="collapsed")
    st.write(":information_source:", sec_metrics_descriptions[sec_metric_selected])
    st.write(":heavy_plus_sign:", sec_metrics_pros[sec_metric_selected])
    st.write(":heavy_minus_sign:", sec_metrics_cons[sec_metric_selected])
    st.write(":pencil2:", sec_metrics_expressions[sec_metric_selected])
    
    st.header("Evaluation des modèles prédictifs")
    st.subheader("Etude comparative")
    st.markdown("""
<p class="normal-font">Dans cette étude, nous avons mené une analyse comparative de différents modèles de classification binaire supervisés pour traiter des jeux de données déséquilibrés. Pour évaluer les performances des modèles, nous avons comparé les performances des modèles avec et sans méthode de rééchantillonnage pour rééquilibrer les données.</p>

<p class="normal-font">Les résultats ont été obtenus en sélectionnant les meilleurs estimateurs à partir d'une grille de paramètres pour chaque modèle. Nous avons utilisé la validation croisée pour consolider les résultats et les avons illustrés à l'aide de <em>courbes ROC</em>, de <em>gain cumulé</em> et de <em>précision-rappel</em>. Nous avons également effectué une analyse basée sur la pondération des classes pour tous les modèles le permettant, et ajusté le seuil de probabilité pour une meilleure distinction des classes.</p>

<p class="normal-font">Les performances de prévision optimales ont été obtenues avec une étape de sous-échantillonnage, elles sont résumées ci-dessous pour chacune des métriques considérées :</p>
""", unsafe_allow_html=True)
    
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
Pour chaque algorithme considéré (à l'exception du modèle KNN), les index 1, 2 et 3 représentent les différentes itérations d'une étude comparative basée le paramétrage de pondération des classes dans la définition du modèle :

- Itération 1 : "class_weight = None"
- Itération 2 : "class_weight = 'balanced'"
- Itération 3 : "class_weight = {0: x, 1: 1-x}"

En outre, pour améliorer la distinction entre les classes, un seuil de probabilité est adapté automatiquement pour tous les modèles. Cela permet de classer les prédictions comme positives ou nulles de manière plus précise.    
""", icon="⚠️")
    
    st.subheader("Choix du meilleur modèle")
    st.markdown("""<p class="normal-font">Les meilleures performances des modèles étudiés sont résumées ci-dessous :</p>""", unsafe_allow_html=True)
    
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
<p class="normal-font">Dans cette étude, nous avons comparé les performances de différents modèles de classification binaire par apprentissage supervisé en utilisant des métriques d'évaluation adaptées aux jeux de données déséquilibrés. Après avoir entraîné ces modèles sur des features sélectionnées à partir de jeux de données nettoyés, nous avons opté pour un modèle de forêt aléatoire en raison de ses performances remarquables.</p>

<p class="normal-font">Les résultats de la validation croisée ont montré que ce modèle présentait une erreur sur le score du jeu de données minime, malgré des traces de sur-entraînement. En termes pratiques, le temps de calcul et les ressources matérielles requises pour ce modèle étaient moins élevés que pour l'autre modèle le plus proche, SVM, et sa capacité d'interprétation des résultats s'est avérée supérieure.</p>

<p class="normal-font">En conséquence, nous avons conclu que <b><font color="#0f8044">le modèle des forêts aléatoires est le plus approprié</font></b> pour résoudre notre problème de classification binaire.</p>
""", unsafe_allow_html=True)
