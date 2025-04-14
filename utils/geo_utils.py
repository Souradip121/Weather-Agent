from shapely.geometry import Point, shape
import geopandas as gpd

# Load GeoJSON for Indian states
gdf = gpd.read_file("https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson")
print("🧠 Available GeoJSON columns:", gdf.columns)

def get_state_from_coords(lat, lon):
    point = Point(lon, lat)
    for _, row in gdf.iterrows():
        if shape(row['geometry']).contains(point):
            return row['NAME_1']
    return "Unknown"
