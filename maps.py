import folium
import geopandas as gpd

# Load a sample geospatial dataset
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Create a Folium map centered around a specific location
m = folium.Map(location=[20, 0], zoom_start=2)

# Add GeoJSON layer
folium.GeoJson(world).add_to(m)

# Save to an HTML file
m.save('world_map.html')

# Display the map
m
