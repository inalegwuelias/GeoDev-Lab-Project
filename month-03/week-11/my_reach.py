import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/amac_wards.gpkg").to_crs(epsg=32632)
drains = gpd.read_file("data/processed/amac_drains.gpkg").to_crs(epsg=32632)

wards["area_km2"] = wards.area / 1_000_000

zone = drains[["geometry"]].copy()
zone["geometry"] = zone.buffer(200)
zone = zone.dissolve()

near = gpd.overlay(wards, zone, how="intersection")
near["near_km2"] = near.area / 1_000_000
result = wards.merge(near[["ward", "near_km2"]], on="ward", how="left")
result["near_km2"] = result["near_km2"].fillna(0)
result["near_pct"] = (result["near_km2"] / result["area_km2"] * 100).round(1)
print(result[["ward", "area_km2", "near_km2", "near_pct"]].round(2))

zone.to_file("data/processed/amac_drain_zone_200m.gpkg", layer="drain_zone")

fig, ax = plt.subplots(figsize=(8, 8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
zone.plot(ax=ax, color="#C0392B", alpha=0.6)
ax.set_title("Land within 200 m of mapped drains, AMAC")
ax.set_axis_off()
fig.savefig("month-03/week-11/my_map.png", dpi=150, bbox_inches="tight")
print("Map saved")