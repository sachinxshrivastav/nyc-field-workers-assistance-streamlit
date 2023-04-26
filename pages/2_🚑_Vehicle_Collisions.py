import streamlit as st
import numpy as np
import pandas as pd
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static

def display_title():
  st.set_page_config(layout="wide")
  st.title('New York City Vehicle Collisions')
  st.markdown("""
  - The application provides users with a comprehensive map of all vehicle collisions that have occurred within the city, including the date, time,location and reason of the collision. 
  - Application helps government agencies to track areas to improve infra and take proactive steps to prevent accdients.
  """)

@st.cache_data
def read_data():
  # Reading the Data from NYC Open Data
  soql_url = ('https://data.cityofnewyork.us/resource/h9gi-nx95.json?' + '$select=crash_date as Crash_Date,latitude,longitude,contributing_factor_vehicle_1 as Reason').replace(' ', '%20')

  # read into pandas as dataframe
  df = pd.read_json(soql_url)

  # Converting DataTime data into proper Format
  df['Crash_Date'] =  pd.to_datetime(df['Crash_Date'])
  df['Crash_Date'] = df['Crash_Date'].dt.strftime('%Y%m%d')
  df = df.dropna()

  return df

@st.cache_data
def draw_kepler_map(df):
  config = {
    'version': 'v1',
    'config': {
        'mapState': {
            'latitude': 40.712776 ,
            'longitude': -74.005974,
            'zoom': 10
        }
        
    }
    }
  map = KeplerGl(height=600, data={"New York City Vehicle Collisions": df}, config=config,)
  keplergl_static(map)
  #map.save_to_html(file_name='data/protected_streets.html',read_only=True, config=config)
  #p = open("data/protected_streets.html")
  #components.html(p.read(),height=600)

def main():
  # Display Map
  display_title()

  # Read Data
  df = read_data()

  draw_kepler_map(df)
    
if __name__ == "__main__":
    main()

