import streamlit as st
import numpy as np
import pandas as pd
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static

def display_title():
  st.set_page_config(layout="wide")
  st.title('New York City Protected Streets')
  st.markdown("""
  - The New York City Protected Streets application is a user-friendly application designed to provide information on the protected streets in New York City. 
  - Field Workers can navigate and find out the protected street segments so that they can plan their construction/repair work.
  - Application gets real-time data updates from NYC Open Data portal.
  - Workers can click on the street segments on the map to view street name and the date from and to till the segment is protected.
  """)

@st.cache_data
def read_data():
  # Reading the Data from NYC Open Data
  soql_url = ('https://data.cityofnewyork.us/resource/wyih-3nzf.json?' + '$select=the_geom,fromstreet as From_Street,tostreetna as To_Street,dateprotec as From_Date,dateprot_1 as To_date').replace(' ', '%20')

  # read into pandas as dataframe
  df = pd.read_json(soql_url)

  # Converting DataTime data into proper Format
  df['From_Date'] =  pd.to_datetime(df['From_Date'])
  df['From_Date'] = df['From_Date'].dt.strftime('%Y%m%d')

  df['To_date'] =  pd.to_datetime(df['To_date'])
  df['To_date'] = df['To_date'].dt.strftime('%Y%m%d')

  return df

@st.cache_data
def draw_kepler_map(df,config):
  map = KeplerGl(height=600, data={"NYC Proteced Streets": df}, config=config)
  keplergl_static(map)
  #map.save_to_html(file_name='data/protected_streets.html',read_only=True, config=config)
  #p = open("data/protected_streets.html")
  #components.html(p.read(),height=600)

def main():
  # Display Map
  display_title()

  # Read Data
  df = read_data()

  config = {'version': 'v1','config': {'mapState': {'latitude': 40.7128 ,'longitude': -74.0060,'zoom': 10}}}

  draw_kepler_map(df,config)
    
if __name__ == "__main__":
    main()