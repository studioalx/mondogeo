import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload, campina, piracuruca  # import your app modules here

st.set_page_config(page_title="STUDIO GEO-MONDO", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": heatmap.app, "title": "PARNAIBA", "icon": "map"},
    {"func": home.app , "title": "PIRACURUCA", "icon": "map"},
    {"func": upload.app, "title": "PIRIPIRI", "icon": "map"},
    {"func": campina.app, "title": "CAMPINA", "icon": "map"},
    {"func": piracuruca.app, "title": "piracuruca 2", "icon": "map"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        Sistema em desenvovilmento, iniciado em 01 de janeiro de 2024, previsao de conclusão dezembro de 2026!!!
        contato studio.alx@outlook.com
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
