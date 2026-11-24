# Week 12: Rasters with Rasterio

## Scene used
- **Scene ID:** LC09_L2SP_189054_20261029_20261031_02_T1
- **Satellite and product:** Landsat 9, Collection 2 Level-2 surface reflectance, Tier 1
- **Date acquired:** 2026-10-29
- **Path / row:** 189 / 054
- **Cloud cover:** [land cloud cover % from the EarthExplorer metadata]
- **Bands used:** SR_B4 (red) and SR_B5 (near-infrared)
- **Source:** USGS EarthExplorer

The rasters themselves are not committed to this repository. They are described in `data-notes.md`.

## What I did
**Guided scripts (Ibadan North teaching data):** inspected a DEM (`inspect_raster.py`), read its values and handled nodata (`read_values.py`), converted between pixels and coordinates (`pixel_coords.py`), sampled elevation at facilities (`sample_points.py`), computed NDVI from Landsat (`ndvi.py`), plotted it (`plot_raster.py`), clipped the DEM to the wards (`clip_raster.py`), calculated mean elevation per ward (`zonal_stats.py`) and reprojected a raster (`reproject_raster.py`). The output map is `ndvi_map.png`.

**Challenge scripts (AMAC, Abuja):**
- `my_inspect.py`: inspected my own Landsat band. [Say whether width times resolution equalled right minus left, and give the numbers.]
- `my_index.py`: computed NDVI for AMAC from bands 4 and 5, applying the Collection 2 scale factor (0.0000275) and offset (-0.2), after converting to float32. NDVI range: [min] to [max]. Mean NDVI: [mean].
- `my_zonal.py`: calculated mean NDVI per AMAC ward. Results are in `amac_zonal.csv`, and the map is `my_map.png`.

## Result
[Two or three sentences on what the ward results show: which wards have the highest and lowest mean NDVI, and what that suggests about vegetation across AMAC. Use your own numbers from `amac_zonal.csv`.]

## CRS
The wards were reprojected to the raster's CRS before the zonal statistics ([raster CRS, e.g. EPSG:32632]). The vector layer is reprojected rather than the raster, so the NDVI values are not resampled.

## Limitation
This is a single date (29 October 2026), so it shows vegetation at one moment and not how it changed through the year. Late October is at the end of the rainy season, so vegetation is likely greener than in the dry season. Landsat pixels are 30 m, which is coarse for small features. [Add anything you noticed about cloud or gaps in the data.]

## Files
- `month-03/week-12/*.py`: guided and challenge scripts
- `ndvi_map.png`: NDVI map from the teaching scene
- `amac_zonal.csv`: mean NDVI per AMAC ward
- `my_map.png`: map of the AMAC results
- `data-notes.md`: description of each raster (not committed)