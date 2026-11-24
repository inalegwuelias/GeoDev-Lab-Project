import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from rasterio.mask import mask

with rasterio.open("data/processed/amac_ndvi.tif") as src:
    wards = gpd.read_file("data/processed/amac_wards.gpkg").to_crs(src.crs)
    means = []
    for geom in wards.geometry:
        cells, _ = mask(src, [geom], crop=True, filled=False)
        cells = np.ma.masked_equal(cells, -9999)
        if cells.count() == 0:
            means.append(np.nan)
        else:
            means.append(float(cells.mean()))

wards["mean_ndvi"] = np.round(means, 3)
print(wards[["ward", "mean_ndvi"]])
wards[["ward", "mean_ndvi"]].to_csv("month-03/week-12/amac_zonal.csv", index=False)

fig, ax = plt.subplots(figsize=(8, 8))
wards.plot(column="mean_ndvi", cmap="RdYlGn", legend=True, ax=ax, edgecolor="white")
ax.set_title("Mean NDVI per ward, AMAC")
ax.set_axis_off()
fig.savefig("month-03/week-12/my_map.png", dpi=150, bbox_inches="tight")
print("Saved CSV and my_map.png")
