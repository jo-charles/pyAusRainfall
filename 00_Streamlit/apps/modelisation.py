import streamlit as st
from PIL import Image

def app():
    st.title("Modélisation des données")
    st.header("Modélisation")
    st.write(
    """Ce projet propose de résoudre un problème de classification binaire avec apprentissage supervisé, car il s'agit de prédire une variable quantitative cible à l'aide d'un ensemble de données étiquetées. Avec des entrées et des sorties étiquetées, le modèle peut mesurer sa précision et apprendre au fil du temps.
    Pour l’élaboration de modèles prédictifs, nous avons eu recours à:
        - des modèles de classification binaire avec apprentissage supervisé de type:
            - régression logistique (“Logistic Regression”)
            - forêts aléatoires (“Random Forest”)
            - séparateurs à vaste marge (“Support Vector Machine”)	
            - K-plus proches voisins (“K-Nearest Neighbors”)
            - arbres de décision (“Decision Tree”)
        - des modèles de séries temporelles multivariées
            """)
    
    st.header("Choix du modèle & Optimisation")
    st.write("""Nous avons essayé 5 modèles de machine learning durant la durée du projet: 
    - Régression Linéaire (lr),
    - Arbres de Décision (dt),
    - K-plus proches voisins (knn), 
    - SVM (svm),
    - Forêt Aléatoire (rf).
"\n\n"
Les meilleures performances obtenues correspondent aux modélisations des prévisions des précipitations avec étape de rééchantillonnage. Elles sont résumées dans le tableau suivant :
""")    
    st.subheader("Resultats")
    st.write("\n\n")  
    img = Image.open("images/results.png")
    st.image(img, width = 600, caption = "")
    