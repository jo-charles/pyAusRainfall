import streamlit as st
from PIL import Image

def app():

    st.title("Modélisation")
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