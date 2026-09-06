# My project brief

## The question
Which areas within 200 metres of natural drainage paths and low-lying land in Abuja Municipal Area Council (AMAC) have lost vegetation cover or gained built-up area since 2015, increasing flood risk?

## Why it matters
Flooding in AMAC (including areas like Wuse 2, Maitama, and Garki) is largely driven by drainage channels being blocked, built over, or losing the vegetation that once absorbed runoff - not by natural waterways overflowing. A map showing where vegetation loss and construction have encroached on natural drainage paths and low-lying land would help residents, planning officers, and drainage maintenance teams identify where flood risk has increased structurally, ahead of the rainy season. I'm also building this as a stepping stone toward a broader Nigeria flood-mapping project I'm working on.

Note on scope: this maps the *conditions* that make flooding worse (built-over drainage lines, stripped vegetation) - it does not capture actual blocked-drain locations or real-time flood events, since that data isn't openly published for Abuja.

## The data I need
- Elevation data (DEM) for AMAC, to identify natural drainage paths and low-lying land
- Land cover / vegetation data, 2015 vs. current, to measure vegetation loss
- Built-up area extent, 2015 vs. current, to measure construction encroachment
- Settlement/building footprints (current), to see what's been built where
- Ward boundary for AMAC, to clip the analysis area
- (Optional) Any mapped drains/canals, as a sanity check against the terrain-derived paths

## Where each dataset comes from
- **Elevation (DEM):** Copernicus GLO-30 Digital Elevation Model, via OpenTopography - https://portal.opentopography.org/dataCatalog (search "Copernicus GLO-30")
- **Land cover / vegetation (2015 vs. current):** ESA WorldCover, or Sentinel-2 imagery via Copernicus Browser - https://esa-worldcover.org/en or https://dataspace.copernicus.eu/browser/
- **Built-up area extent (multiple years):** GRID3 NGA Settlement Extents (versioned releases), Humanitarian Data Exchange - https://data.humdata.org/dataset/37a5d802-6867-4429-aaad-737b03e5ee8f
- **Settlement/building footprints (current):** GRID3 NGA Settlement Extents v4.0, or OpenStreetMap buildings (Geofabrik Nigeria extract) - https://download.geofabrik.de/africa/nigeria.html
- **Ward boundary (AMAC):** GRID3 NGA Operational Ward Boundaries, Humanitarian Data Exchange - https://data.humdata.org/group/nga (search "FCT Operational Ward Boundaries")
- **Mapped drains/canals (optional):** OpenStreetMap Nigeria extract (Geofabrik), waterway=drain/canal tags - https://download.geofabrik.de/africa/nigeria.html

## What I would build
A map of AMAC shaded by flood risk exposure - combining terrain-derived drainage paths/low-lying land with vegetation loss and built-up expansion since 2015 - so a viewer can see at a glance where encroachment has increased flood risk. Eventually this could feed into a dashboard an officer could open before rainy season, or one that updates as new imagery becomes available.