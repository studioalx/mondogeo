import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIAUI")

    st.markdown(
        """
    sistema em desenvolvimento

    """
    )

    m = leafmap.Map(locate_control=True,location=[-41.687117658472058,31.522959762553785], zoom_start=10, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
