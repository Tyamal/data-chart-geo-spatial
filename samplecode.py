import geopandas as gpd
import matplotlib.pyplot as plt

# Load a sample geospatial dataset (e.g., world countries)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Create a new column for demonstration purposes
# For example, let's say we want to visualize population density
world['pop_density'] = world['pop_est'] / world['area']

# Plotting
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1)
world.plot(column='pop_density', ax=ax, legend=True,
           legend_kwds={'label': "Population Density by Country",
                        'orientation': "horizontal"},
           cmap='OrRd')

# Title and labels
plt.title('World Population Density')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Show the plot
plt.show()
