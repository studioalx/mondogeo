import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIAUI")

    st.markdown(
        """
    sistema em desenvolvimento

    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
