import rasterio

PATH = "data/raw/landsat/LC09_L2SP_189054_20261029_20261031_02_T1_SR_B4.TIF"

with rasterio.open(PATH) as src:
    print("Width x height:", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data type:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src.bounds)
    print("Nodata:", src.nodata)
    print(src.transform)

    print("Width x resolution:", src.width * src.res[0])
    print("Right minus left:", round(src.bounds.right - src.bounds.left, 1))
    print("Height x resolution:", src.height * src.res[1])
    print("Top minus bottom:", round(src.bounds.top - src.bounds.bottom, 1))
