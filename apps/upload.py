import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIRIPIRI - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-4.28,-41.77], zoom_start=15, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
