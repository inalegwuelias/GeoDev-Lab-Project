import geopandas as gpd

wards = gpd.read_file("data/processed/amac_wards.gpkg").to_crs(epsg=32632)
print("Invalid before:", (~wards.is_valid).sum())
wards["geometry"] = wards.make_valid()
print("Invalid after:", (~wards.is_valid).sum())