import csv


def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }


area_result = inspect_column("drainage_buffer.csv", "area_km2")
precise_result = inspect_column("drainage_buffer.csv", "area_km3")
print("Area km2 (rounded):", area_result)
print("Area km3 field (precise km2):", precise_result)