import streamlit as st
from multiapp import MultiApp
from apps import introduction, pretraitement, visualisation, modelisation, demonstration, conclusion

st.set_page_config(layout="wide")

apps = MultiApp()

# Add all your application here
apps.add_app("Introduction", introduction.app)
apps.add_app("Prétraitement", pretraitement.app)
apps.add_app("Visualisation", visualisation.app)
apps.add_app("Modélisation", modelisation.app)
apps.add_app("Démonstration", demonstration.app)
apps.add_app("Conclusion", conclusion.app)

# The main app
apps.run()

with st.sidebar:
    st.markdown("""
    **Promotion DS Continu - Avril 2022**

    Réalisé par :
    - Anne-Claire OGIERAIKHI
    - Joseph CHARLES ([Linkedin](https://fr.linkedin.com/in/josephcharles1))
    - Olivier AMABLE ([Linkedin](https://fr.linkedin.com/in/olivier-amable))
    - Geneviève STEELE
    
    Encadré par : 
    - Laurène BOUSKILA
    """)