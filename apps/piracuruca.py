import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIRACURUCA - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-3.9336,-41.7085], zoom_start=12, tiles="OpenStreetMap")

    #bairros = giseo.GeoDataFrame("https://geojson.io/api/geojson/5e8f131f7a73104a9c3e8f12/geojson")


    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
