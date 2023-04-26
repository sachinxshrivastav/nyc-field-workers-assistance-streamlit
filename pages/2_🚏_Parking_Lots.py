import streamlit as st
import numpy as np
import pandas as pd
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static


def display_title():
    st.set_page_config(layout="wide")
    st.title('New York City Parking Lots')
    st.markdown("""
    - The application provides location of all the parking lots in the New York City.
    """)

@st.cache_data
def read_data():
    # Reading from Geojson File
    with open('data/Parking Lot.geojson', 'r') as f:
        geojson_file = f.read()

    df = geojson_file
    return df

@st.cache_data(show_spinner=False)
def draw_kepler_map(df,config):
    map = KeplerGl(height=600, data={"New York City Parking Lots": df}, config=config)
    keplergl_static(map) 

def main():
    # Display Map
    display_title()

    # Read Data
    df = read_data()

    # Map Config    
    config = {'version': 'v1','config': {'mapState': {'latitude': 40.7128 ,'longitude': -74.0060,'zoom': 9}}, } 

    draw_kepler_map(df,config)

if __name__ == "__main__":
    main()

