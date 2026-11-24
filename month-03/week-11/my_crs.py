import geopandas as gpd

wards = gpd.read_file("data/processed/amac_wards.gpkg")
print("CRS:", wards.crs)
print("Suggested UTM:", wards.estimate_utm_crs())

wards_utm = wards.to_crs(epsg=32632)
wards_utm["area_km2"] = wards_utm.area / 1_000_000
print(wards_utm[["ward", "area_km2"]].round(2))
print("AMAC total:", round(wards_utm["area_km2"].sum(), 1), "km2")

drains = gpd.read_file("data/processed/amac_drains.gpkg").to_crs(epsg=32632)
print("Drain length:", round(drains.length.sum() / 1000, 1), "km")