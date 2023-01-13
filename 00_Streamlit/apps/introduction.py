import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gpd

DATASET_FOLDER = '../data/'

def app():
    st.title("Présentation du projet")
    st.header("Contexte et objectif")
    st.markdown("""
    Ce projet porte sur l'étude d'une série chronologique regroupant environ 10 années d'observations météorologiques quotidiennes en Australie.
    
    L'objectif principal est de prédire les précipitations du jour suivant l'observation à l'aide de la variable cible "RainTomorrow".
    
    Le sujet proposé permet la mise en pratique des connaissances acquises pendant la formation.
    """)
    
    st.subheader("Sources de données")
    st.markdown("""
    The Bureau of Meteorology in Australia :
    http://www.bom.gov.au/climate/data/
    
    Ces données sont également disponibles librement sur le site Kaggle à partir du lien suivant : https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package
    """)      

    st.subheader("Chiffres clés")
    st.markdown("""
    Les données disponibles vont de 2008 à 2017 et concernent 49 villes d'Australie.
    
    Le jeu de données se compose de 23 variables et 145 460 observations.
    
    La pluviométrie annuelle moyenne varie de 300 mm à 1 400 mm dans les zones les plus humides.
    A titre de comparaison, les précipitations annuelles moyennes en France métropolitaine s’échelonnent de 500 à 2000 mm par an.
    
    """)
    
    data_load_state = st.text('Loading data...')
    df = pd.read_csv(DATASET_FOLDER + "weatherAUS.csv")
    data_load_state.text("")
    
    # création d'un dataframe avec les villes australiennes et les latitudes et longitudes correspondantes
    ar = np.array([['Albury',-36.0810,146.9185], ['BadgerysCreek',-33.8874,150.7405], ['Cobar',-31.4949,145.8401],
                   ['CoffsHarbour',-30.29702,153.1151], ['Moree',-29.4644,149.8451], ['Newcastle',-32.9284,151.7606],
                   ['NorahHead',-33.2825,151.5741], ['NorfolkIsland',-29.0408,167.9552], ['Penrith',-33.7511,150.6942],
                   ['Richmond',-33.5983,150.7511], ['Sydney',-33.8650,151.2094], ['SydneyAirport',-33.9473,151.1794],
                   ['WaggaWagga',-35.1171,147.3567], ['Williamtown',-32.8150,151.8427], ['Wollongong',-34.4331,150.8831],
                   ['Canberra',-35.2931,149.1269], ['Tuggeranong',-35.4244,149.0888], ['MountGinini',-35.5293,148.7722],
                   ['Ballarat',-37.5500,143.8500], ['Bendigo',-36.7500,144.2667], ['Sale',-38.1000,147.0667],
                   ['MelbourneAirport',-37.6712,144.8511], ['Melbourne',-37.8136,144.9631], ['Mildura',-34.1889,142.1583],
                   ['Nhil',-36.3327,141.6503], ['Portland',-38.3333,141.6000], ['Watsonia',-37.7113,145.0827],
                   ['Dartmoor',-37.9222,141.2749], ['Brisbane',-27.4678,153.0281], ['Cairns',-16.9303,145.7703],
                   ['GoldCoast',-28.0166,153.3999], ['Townsville',-19.2564,146.8183], ['Adelaide',-34.9289,138.6011],
                   ['MountGambier',-37.8294,140.7827], ['Nuriootpa',-34.4667,138.9833], ['Woomera',-31.1998,136.8325],
                   ['Albany',-35.0228,117.8814], ['Witchcliffe',-34.0260,115.0999], ['PearceRAAF',-31.6677,116.0090],
                   ['PerthAirport',-31.9410,115.9742], ['Perth',-31.9522,115.8589], ['SalmonGums',-32.9763,121.6422],
                   ['Walpole',-34.9550,116.7696], ['Hobart',-42.8806,147.3250], ['Launceston',-41.4419,147.1450],
                   ['AliceSprings',-23.6974,133.8836], ['Darwin',-12.4381,130.8411], ['Katherine',-14.4667,132.2667],
                   ['Uluru',-25.3444,131.0354]])
    
    df1 = pd.DataFrame(ar, columns=['Ville', 'Latitude', 'Longitude'])
    df1.Latitude = df1.Latitude.astype(float)
    df1.Longitude = df1.Longitude.astype(float)
    
    # fusion du dataframe précédent avec le dataframe principale df
    df2 = df.groupby('Location').sum()
    df_lat_long = df1.merge(df2, left_on="Ville", right_on="Location")
    
    # cartographie des précipitations
    fig,ax = plt.subplots(figsize=(10,8))
    countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    countries[countries["name"]=="Australia"].plot(color="lightgrey", ax=ax)
    
    df_lat_long.plot.scatter(x='Longitude', y='Latitude', c='Rainfall', cmap='viridis',
                             title="Précipitations en mm de 2008 à 2017",ax=ax)
    ax.grid(b=True,alpha=0.5)
    
    st.pyplot(fig)