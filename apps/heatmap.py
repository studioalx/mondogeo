import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PARNAIBA - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-2.927,-41.745], zoom_start=13, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
