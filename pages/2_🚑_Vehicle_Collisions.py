import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium, folium_static
import time


st.write('## NYC Vehicle Collisions')

with st.spinner("Loading..."):
  time.sleep(5)


soql_url = ('https://data.cityofnewyork.us/resource/h9gi-nx95.json?' + '$select=crash_date,crash_time,latitude,longitude').replace(' ', '%20')

# read into pandas as dataframe
df = pd.read_json(soql_url)

df = df.dropna()

latitude = 40.712776
longitude = -74.005974

nyc_map = folium.Map(location = [latitude, longitude], zoom_start = 10)

incidents_accident = folium.map.FeatureGroup()
latitudes = list(df.latitude)
longitudes = list(df.longitude)
labels = list(df.crash_time)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker(
      location = [lat, lng], 
      popup = label,
      icon = folium.Icon(color='red', icon='info-sign')
     ).add_to(nyc_map)

st_data = folium_static(nyc_map, width=700)