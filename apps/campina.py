import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("CAMPINA GRANDE - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-7.235,-35.900], zoom_start=12.5, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
