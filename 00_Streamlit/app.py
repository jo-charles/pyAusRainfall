import streamlit as st
from multiapp import MultiApp
from apps import introduction, pretraitement, visualisation, modelisation, demonstration, conclusion

st.set_page_config(layout="wide")

apps = MultiApp()

apps.add_app("Introduction (Olivier)", introduction.app)
apps.add_app("Prétraitement (Olivier)", pretraitement.app)
apps.add_app("Visualisation (Anne-Claire)", visualisation.app)
apps.add_app("Modélisation (Joseph)", modelisation.app)
apps.add_app("Démonstration (Geneviève)", demonstration.app)
apps.add_app("Conclusion (Olivier)", conclusion.app)

apps.run()

with st.sidebar:
    st.markdown("""
    ## **Promotion DS Continu - Avril 2022**

    ### Réalisé par :
    - Anne-Claire OGIERAIKHI
    - Joseph CHARLES ([Linkedin](https://fr.linkedin.com/in/josephcharles1))
    - Olivier AMABLE ([Linkedin](https://fr.linkedin.com/in/olivier-amable))
    - Geneviève STEELE
    
    ### Encadré par : 
    - Laurène BOUSKILA
    """)