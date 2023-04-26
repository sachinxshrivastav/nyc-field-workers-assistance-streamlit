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
    return map

    
    

def main():
    # Display Map
    display_title()

    # Read Data
    df = read_data()

    # Map Config    
    #config = {'version': 'v1','config': {'mapState': {'latitude': 40.7128 ,'longitude': -74.0060,'zoom': 9}}, } 

    config = {'version': 'v1',
 'config': {'visState': {'filters': [],
   'layers': [{'id': 'hfw7mx',
     'type': 'geojson',
     'config': {'dataId': 'data_1',
      'label': 'data_1',
      'color': [195, 40, 153],
      'highlightColor': [252, 242, 26, 255],
      'columns': {'geojson': '_geojson'},
      'isVisible': True,
      'visConfig': {'opacity': 0.8,
       'strokeOpacity': 0.8,
       'thickness': 0.5,
       'strokeColor': [221, 178, 124],
       'colorRange': {'name': 'UberPool 6',
        'type': 'diverging',
        'category': 'Uber',
        'colors': ['#213E9A',
         '#551EAD',
         '#C019BD',
         '#D31256',
         '#E6470A',
         '#F9E200']},
       'strokeColorRange': {'name': 'Global Warming',
        'type': 'sequential',
        'category': 'Uber',
        'colors': ['#5A1846',
         '#900C3F',
         '#C70039',
         '#E3611C',
         '#F1920E',
         '#FFC300']},
       'radius': 10,
       'sizeRange': [0, 10],
       'radiusRange': [0, 50],
       'heightRange': [0, 500],
       'elevationScale': 5,
       'enableElevationZoomFactor': True,
       'stroked': False,
       'filled': True,
       'enable3d': False,
       'wireframe': False},
      'hidden': False,
      'textLabel': [{'field': None,
        'color': [255, 255, 255],
        'size': 18,
        'offset': [0, 0],
        'anchor': 'start',
        'alignment': 'center'}]},
     'visualChannels': {'colorField': {'name': 'shape_area', 'type': 'real'},
      'colorScale': 'quantile',
      'strokeColorField': None,
      'strokeColorScale': 'quantile',
      'sizeField': None,
      'sizeScale': 'linear',
      'heightField': None,
      'heightScale': 'linear',
      'radiusField': None,
      'radiusScale': 'linear'}}],
   'interactionConfig': {'tooltip': {'fieldsToShow': {'data_1': [{'name': 'shape_area',
        'format': None},
       {'name': 'shape_leng', 'format': None},
       {'name': 'feat_code', 'format': None},
       {'name': 'status', 'format': None},
       {'name': 'sub_code', 'format': None}]},
     'compareMode': False,
     'compareType': 'absolute',
     'enabled': True},
    'brush': {'size': 0.5, 'enabled': False},
    'geocoder': {'enabled': False},
    'coordinate': {'enabled': False}},
   'layerBlending': 'normal',
   'splitMaps': [],
   'animationConfig': {'currentTime': None, 'speed': 1}},
  'mapState': {'bearing': 0,
   'dragRotate': False,
   'latitude': 40.47305093168668,
   'longitude': -73.90659639144137,
   'pitch': 0,
   'zoom': 8.711546639647146,
   'isSplit': False},
  'mapStyle': {'styleType': 'dark',
   'topLayerGroups': {},
   'visibleLayerGroups': {'label': True,
    'road': True,
    'border': False,
    'building': True,
    'water': True,
    'land': True,
    '3d building': False},
   'threeDBuildingColor': [9.665468314072013,
    17.18305478057247,
    31.1442867897876],
   'mapStyles': {}}}}

    draw_kepler_map(df,config)

   
    
if __name__ == "__main__":
    main()

