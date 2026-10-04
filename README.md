# Flood Risk Mapping — AMAC, Abuja

**Question:** Which areas within 200 metres of natural drainage paths and low-lying land in Abuja Municipal Area Council (AMAC) have lost vegetation cover or gained built-up area since 2015, increasing flood risk?

Flooding in AMAC is largely driven by drainage channels being blocked, built over, or stripped of vegetation — not by rivers overflowing. This project uses open geospatial data to identify where terrain, drainage proximity, and built-up growth intersect to increase flood risk, since blocked-drain locations themselves aren't openly published for Abuja.

## Month 1 result

A 200-metre buffer was built around all OpenStreetMap-mapped drainage lines in AMAC. Intersecting this buffer with AMAC building footprints shows **[X] buildings** currently sit within 200 metres of a mapped drainage path — a real, if partial, measure of structures exposed to drainage-related flood risk in AMAC today. OSM's drainage coverage for AMAC is sparse, which itself confirms the project's premise: open data cannot show blocked or built-over drains directly, so proximity and land-use proxies are needed instead.

## Project structure
- **[Week 1 — Project Brief](week1-project-brief/project-brief.md)** — the question, why it matters, and a source link for every dataset needed.
- **[Week 2 — Data Notes](week2-data-notes/data-notes.md)** — what was downloaded, feature counts, columns, and gaps found.
- **[Week 3 — Data Preparation](week3-data-preparation/data-notes.md)** — CRS identification, reprojection to EPSG:32632, area calculations, and quality checks.
- **[Week 4 — Analysis](week4-analysis/month-1-summary.md)** — the 200m drainage buffer, building-exposure intersection, four-way validation, and the map of the result.

## Status
Vegetation/land-cover and elevation (DEM) layers are still needed to complete the full flood-risk classification described in the original question. This month's result is a partial, honest answer based on drainage proximity and building exposure alone.

## Note on large files
`buildings_amac_utm32.gpkg` and `buildings_in_buffer.gpkg` exceed GitHub's file size limit and are not committed to this repository. They were generated locally following the steps in this summary (OSM buildings via Overpass Turbo, clipped to AMAC, reprojected to EPSG:32632, intersected with the 200m drainage buffer). The resulting building-exposure count (see Month 1 result above) is derived from these files.

## Month 2: development environment and early python
Week 5: set up Python, VS code and terminal. hello.py runs.
