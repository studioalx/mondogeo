import streamlit as st
import leafmap.foliumap as leafmap
#**********************************************************************
"""
import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("MAPA PIRACURUCA - VERSÃO DE TESTE")

    

    m = leafmap.Map(locate_control=True,location=[-3.935,-41.710], zoom_start=14, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)
"""
#**********************************************************************
def app():
st.title("Mapa de Piracuruca com Limites de Bairros")

   m = leafmap.Map(locate_control=True,location=[-3.935,-41.710], zoom_start=14, tiles="OpenStreetMap")
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=800)

# Carregar os dados dos bairros
bairros = giseo.GeoDataFrame("https://geojson.io/api/geojson/5e8f131f7a73104a9c3e8f12/geojson")

# Adicionar estilo aos bairros
bairros.style["fillColor"] = "lightblue"
bairros.style["stroke"] = "blue"
bairros.style["linewidth"] = 1

# Exibir os bairros no mapa
map.add_layer(bairros)

# Exibir o nome de Piracuruca no mapa
map.add_text(
    text="Piracuruca",
    location=piracuruca_center,
    color="red",
)
