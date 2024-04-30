import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregando dados da capital e dos municípios do Piauí
capitais_df = pd.read_csv("https://dados.gov.br/pt-br/dataset/ibge-codigos-municipios")
municipios_df = pd.read_csv("https://dados.gov.br/pt-br/dataset/ibge-mapa-municipio")

# Filtrando dados do Piauí
capitais_df_piaui = capitais_df[capitais_df["sigla_uf"] == "PI"]
municipios_df_piaui = municipios_df[municipios_df["sigla_uf"] == "PI"]

# Criando o mapa
centroide_piaui = [-5.135458, -42.730791]  # Coordenadas do centroide do Piauí
fig, ax = plt.subplots()

# Adicionando municípios ao mapa
for i in range(len(municipios_df_piaui)):
    x = municipios_df_piaui["lon"][i]
    y = municipios_df_piaui["lat"][i]
    ax.plot(x, y, marker="o", markersize=5, color="blue", alpha=0.7)

# Adicionando capital ao mapa
ax.plot(
    capitais_df_piaui["lon"].values[0],
    capitais_df_piaui["lat"].values[0],
    marker="s",
    markersize=10,
    color="red",
    label="Teresina",
)

# Ajustando o mapa
ax.set_title("Mapa do Piauí")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_xlim([-5.4, -42.4])
ax.set_ylim([-9.2, -4.8])
ax.legend()

# Mostrando o mapa no Streamlit
st.title("Mapa do Piauí")
st.map(fig)
