import geopandas as gpd

wards = gpd.read_file("data/processed/amac_wards.gpkg").to_crs(epsg=32632)
buildings = gpd.read_file("data/processed/amac_building_points.gpkg").to_crs(epsg=32632)

joined = gpd.sjoin(buildings, wards[["ward", "geometry"]], how="inner", predicate="within")
counts = joined.groupby("ward").size().rename("building_count").reset_index()
wards = wards.merge(counts, on="ward", how="left")
wards["building_count"] = wards["building_count"].fillna(0).astype(int)
print(wards[["ward", "building_count"]])
print("Total counted:", wards["building_count"].sum(), "of", len(buildings))