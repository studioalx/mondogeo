import pydeck as pdk
import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

centroids = gpd.GeoDataFrame()
centroids["geometry"] = world.geometry.centroid
centroids["name"] = world.name



pdk.Deck(layers, map_provider=None).to_html("geopandas_integration.html", css_background_color="cornflowerblue")
