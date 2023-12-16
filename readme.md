HOW TO START THE PROJECT:
* First install requirements:
 pip3 install -r requirements.txt

* Run the main.py file


OTHER INFORMATION:
The *normalized difference vegetation index (NDVI)* is a widely-used metric for quantifying the health and density of
vegetation using remote sensors, such as satellites.

NDVI PROPERTIES:
* NDVI will be a value between -1 and 1.
* An area with nothing growing in it will have an NDVI of zero.
* NDVI will increase in proportion to vegetation growth.
* An area with dense, healthy vegetation will have an NDVI of one

*Sentinel 2 imagery* typically refers to the satellite imagery captured by the Sentinel-2 satellites, which is
designed to provide high-resolution optical imagery of the Earth's surface.

We are extracting a portion of a Sentinel 2 imagery dataset that corresponds to a specific geographic area defined by a
*Polygon*, which is mentioned as sample_polygon.json in polygon directory

ADDITIONAL INFORMATION ABOUT THE TOOLS AND TERMINOLOGY:

* We're opening the satellite imagery (like a big digital photo) using a tool called rioxarray.
  This tool helps us work with geospatial data.

* As a Rasterio Xarray, we can think of it like a super smart version of an image file.
  This "xarray" knows not just about the colors in the image but also understands the spatial information,
  like where each pixel is on the Earth.


STATISTICS:

We are using NumPy to calculate these values:
* Minimum: Least vegetation in the particular area
* Maximum: Most vegetation in the particular area
* Mean: Average vegetation in the particular area

