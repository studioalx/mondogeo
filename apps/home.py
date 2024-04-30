import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIAUI - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-3.50,-41.522959762553785], zoom_start=10, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
