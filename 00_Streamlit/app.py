import streamlit as st
from multiapp import MultiApp
from apps import projet, analyse, modelisation, datasets, methodologie, prediction, conclusion

st.set_page_config(layout="wide")

apps = MultiApp()

# Add all your application here
apps.add_app("Projet", projet.app)
apps.add_app("Dataset", datasets.app)
apps.add_app("Analyse", analyse.app)
apps.add_app("Méthodologie", methodologie.app)
apps.add_app("Modélisation", modelisation.app)
apps.add_app("Prédiction", prediction.app)
apps.add_app("Conclusion", conclusion.app)

# The main app
apps.run()

with st.sidebar:
    st.write("""
    **Promotion DS Continu - Avril 2022**

    Réalisé par :
    - Anne-Claire OGIERAIKHI
    - Joseph CHARLES ([Linkedin](https://fr.linkedin.com/in/josephcharles1))
    - Olivier AMABLE
    - Geneviève STEELE
    
    Encadré par : 
    - Laurène BOUSKILA
    """)