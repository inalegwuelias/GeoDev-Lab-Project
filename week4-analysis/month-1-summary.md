# Month 1 Summary

## The question
Which areas within 200 metres of natural drainage paths and low-lying land in Abuja Municipal Area Council (AMAC) have lost vegetation cover or gained built-up area since 2015, increasing flood risk?

## Operation run
Ran a 200-metre buffer on OpenStreetMap waterway/drain lines within AMAC (queried via QuickOSM, scoped using the layer extent of the AMAC ward boundary to avoid Nominatim API timeouts), in EPSG:32632 (UTM Zone 32N). A fixed-distance buffer around drainage paths was chosen because it directly operationalizes the "within 200 metres" condition already stated in my research question, rather than being a separate demonstration exercise.

## Expected vs. got
Expected: given how sparsely drainage infrastructure is mapped in OpenStreetMap for Abuja, I expected the query to return a small number of waterway features and a correspondingly small, scattered buffer area — likely well under [your estimate] km² total, not a continuous zone across AMAC.

Got: the query returned [X] waterway/drain features. After buffering by 200 metres and dissolving overlaps, the result was [Y] buffer polygon(s) covering approximately [Z] km² in total.

## Checks performed
1. **Map check:** visually inspected the buffer layer against the AMAC ward boundary — buffers appeared only around the queried drainage lines, at a consistent width, with no buffer extending implausibly far from its source line.
2. **Row count check:** buffer feature count ([Y]) was [consistent with / lower than] the input drainage line count ([X]), as expected after dissolving overlapping buffers.
3. **Manual verification:** selected one buffer polygon and measured its area using the field calculator ($area). For a line segment of approximately [length] m, a 200 m buffer should produce roughly length × 400 m (both sides) plus rounded end caps — the measured area of [value] km² was [consistent with / different from] this rough estimate.
4. **Empty geometry check:** ran Vector → Geometry Tools → Check Validity on the buffer layer; [no invalid or null geometries were found / found and noted below].

## What surprised me
OpenStreetMap's drainage/waterway coverage for AMAC turned out to be [very sparse / sparser than expected / more complete than expected], which [confirms / complicates] the project's underlying assumption that open geospatial data cannot directly show blocked or built-over drains in Abuja. This reinforces why the project uses terrain and land-cover change as a proxy for drainage-related flood risk, rather than relying on mapped drainage infrastructure directly.

## What I still need
- Vegetation/land cover data (2015 vs. current) to identify actual vegetation loss within the 200 m buffer zone
- Built-up area layers (multiple years) to identify construction encroachment within the buffer
- Elevation (DEM) data to identify low-lying land, still not yet incorporated
- Remaining datasets from Week 2 still need clipping and reprojecting, per prior feedback
  
## Additional data: buildings
After the initial buffer analysis, building footprints for AMAC were obtained (via Overpass Turbo, OSM building data) and clipped/reprojected to match the drainage buffer analysis. Intersecting the buildings layer with the 200m drainage buffer shows [X] buildings currently sit within 200 metres of mapped drainage paths in AMAC — indicating direct, identifiable exposure to blocked or overflow-prone drainage lines, even before vegetation-loss or elevation data is incorporated.
