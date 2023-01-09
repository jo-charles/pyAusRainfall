import streamlit as st


def app():

    st.title("Méthodologie")
    st.header("Classification du problème")
    st.write("\n\n")  
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
