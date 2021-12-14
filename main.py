import datetime
import folium
import geopandas as gpd
import geopy
import networkx as nx
import osmnx as ox
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import time

from folium.features import DivIcon
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from PIL import Image
from streamlit_folium import folium_static



st.set_page_config(
    page_title="Mexico Illegal Dumpsites",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.markdown('<h1 style="margin-left:8%; color:#1a5276">Fighting illegal dumping in Mexico</h1>', unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "",
    ("About", "Dataset", "EDA", "Modelling", "Collaborators")
)

if add_selectbox == 'About':
    st.subheader('ABOUT THE PROJECT')

    st.markdown('<h4>The Background</h4>', unsafe_allow_html=True)
    st.markdown('Environmental conservation has many different factors, and in Mexico, one of the most influential is the relationship \
        between dumping sites and garbage collection. Many places in Mexico are severely affected illegally, and some of them are regions \
            of nature that must be protected', unsafe_allow_html=True)
    st.markdown('<h4>The Problem</h4>', unsafe_allow_html=True)

    
    st.markdown('Build machine learning models on illegal dumping(s)in Mexico to see if there are any patterns to help understand what \
        causes illegal dumping(s), predict potential dumpsites, and eventually how to avoid them.', 
        unsafe_allow_html=True)

    # st.markdown('<h4>Locations Reported as Illegal Dumpsites</h4>', unsafe_allow_html=True)

    #st.image('dumpsitemap.PNG')


elif add_selectbox == 'Dataset':
    st.subheader('Dataset')

    st.image('trashout.PNG')
    st.image('dumpsites.PNG')
    # st.image('wikipedia.PNG')

elif add_selectbox == 'EDA':
    st.subheader('Exploratory Data Analysis')

    eda = st.selectbox(
     'Select Model',
     ('Trash Details','Location', 'Waste Management', 'Population'))

    if eda == 'Trash Details':
        st.image('type_of_trash.PNG')
        st.image('size_of_trash.PNG')
    elif eda == 'Location':
        st.image('top_states.PNG')
        st.image('top_cities.PNG')
    elif eda == 'Waste Management':
        st.image('waste_management.PNG')
    elif eda == 'Population':
        st.image('population.PNG')
        st.image('area.PNG')
        st.image('density.PNG')


elif add_selectbox == 'Modelling':
    st.subheader('Modelling')

    modeling_option = st.selectbox(
     'Select Model',
     ('Computer Vision','Clustering'))

    if modeling_option == 'Computer Vision':
        st.image('computer_vision_1.PNG')
        st.image('computer_vision_2.PNG')
        st.image('computer_vision_3.PNG')



elif add_selectbox == 'Collaborators':
    st.subheader('Collaborators')

    st.markdown('<a href="https://omdena.com/omdena-chapter-page-mexico/" target="_blank">Omdena Mexico Chapter</a>', unsafe_allow_html=True)

    st.markdown('Project Managers: <a href="https://www.linkedin.com/in/emmanuel-rotm/" target="_blank">Mario Rodriguez</a>, <a href="https://www.linkedin.com/in/emmanuel-rotm/" target="_blank">Vic</a>', unsafe_allow_html=True)
    st.markdown('Members:', unsafe_allow_html=True)
    st.markdown('<ul>\
        <li><a href="https://www.linkedin.com/in/cesartinocoa/" target="_blank">Cesar Tinoco</a></li>\
        <li><a href="https://www.linkedin.com/in/rhey-ann-magcalas-47541490/" target="_blank">Rhey Ann Magcalas</a></li></ul>', unsafe_allow_html=True)
