import streamlit as st

st.title("Mapa de Piracuruca com Limites de Bairros")

# Definir a centralização do mapa
piracuruca_center = (-5.711111, -42.777778)

# Criar o mapa
map = st.map(center=piracuruca_center, zoom=10)

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