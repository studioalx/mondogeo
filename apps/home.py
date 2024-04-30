import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIRACURUCA - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-4.59,-41.59], zoom_start=13, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
