import folium
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium, folium_static
import time

soql_url = ('https://data.cityofnewyork.us/resource/wyih-3nzf.json?' + '$select=the_geom,fromstreet,tostreetna,dateprotec,dateprot_1').replace(' ', '%20')

# read into pandas as dataframe
df = pd.read_json(soql_url)

# Converting to DateTime
df['dateprotec'] =  pd.to_datetime(df['dateprotec'])
df['dateprot_1'] = pd.to_datetime(df['dateprot_1'])


# Creating Folium Map
# Load map using your origin latlong
my_map = folium.Map(location=[40.712776,-74.005974,],
                    zoom_start=12,
                    tiles='OpenStreetMap')
for i in range(len(df['the_geom'])):
    my_PolyLine=folium.PolyLine(locations=[v[::-1] for v in df['the_geom'][i]['coordinates'][0]]
    ,tooltip=f"{df['fromstreet'][i]} - {df['tostreetna'][i]} <br> {df['dateprotec'][i]} - {df['dateprot_1'][i]} "
    ,weight=2,color='red')
    my_map.add_child(my_PolyLine)

st.write('## NYC Protected Streets')

with st.spinner("Loading..."):
  time.sleep(5)

st_data = folium_static(my_map, width=700)
