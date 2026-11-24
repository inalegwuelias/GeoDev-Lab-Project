import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

FOLDER = "data/raw/landsat/"
SCENE = "LC09_L2SP_189054_20261029_20261031_02_T1"


def read_clipped(path, geoms):
    with rasterio.open(path) as src:
        data, transform = mask(src, geoms, crop=True, nodata=0)
        profile = src.profile
    return data[0].astype("float32"), transform, profile


with rasterio.open(FOLDER + SCENE + "_SR_B4.TIF") as src:
    raster_crs = src.crs

wards = gpd.read_file("data/processed/amac_wards.gpkg").to_crs(raster_crs)
geoms = [wards.dissolve().geometry.iloc[0]]

red_raw, transform, profile = read_clipped(FOLDER + SCENE + "_SR_B4.TIF", geoms)
nir_raw, _, _ = read_clipped(FOLDER + SCENE + "_SR_B5.TIF", geoms)

valid = (red_raw > 0) & (nir_raw > 0)
red = red_raw * 0.0000275 - 0.2
nir = nir_raw * 0.0000275 - 0.2

ndvi = np.full(red.shape, -9999, dtype="float32")
total = nir + red
ok = valid & (total != 0)
ndvi[ok] = (nir[ok] - red[ok]) / total[ok]
print("NDVI range:", round(float(ndvi[ok].min()), 3), "to", round(float(ndvi[ok].max()), 3))
print("Mean NDVI:", round(float(ndvi[ok].mean()), 3))

profile.update(
    dtype="float32", nodata=-9999, count=1,
    height=ndvi.shape[0], width=ndvi.shape[1], transform=transform, tiled=False,
)
profile.pop("blockxsize", None)
profile.pop("blockysize", None)
with rasterio.open("data/processed/amac_ndvi.tif", "w", **profile) as dst:
    dst.write(ndvi, 1)
print("Saved data/processed/amac_ndvi.tif")
