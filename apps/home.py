import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIRACURUCA - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-3.93,-41.710], zoom_start=14, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
