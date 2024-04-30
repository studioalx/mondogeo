import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIRACURUCA - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-3.00,-41.0], zoom_start=10, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
