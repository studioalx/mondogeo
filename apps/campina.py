import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIRACURUCA - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-3.935,-20.710], zoom_start=12, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
