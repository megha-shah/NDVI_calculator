import rasterio
import geopandas as gpd
import rioxarray
import matplotlib.pyplot as plt


class NDVICalculator:
    def __init__(self, sentinel_band_uri_1, sentinel_band_uri_2, polygon_path, output_ndvi_png, colormap='viridis',
                 chunk_size=(1000, 1000), png_label='NDVI'):
        self._sentinel_band_uri_1 = sentinel_band_uri_1
        self._sentinel_band_uri_2 = sentinel_band_uri_2
        self._polygon_path = polygon_path
        self.output_ndvi_png = output_ndvi_png

        self.colormap = colormap
        self.chunk_size = chunk_size
        self.png_label = png_label

        self.band_subset_1 = None
        self.band_subset_2 = None
        self.ndvi_array = None

    def get_sentinel_band_uri_1(self):
        return self._sentinel_band_uri_1

    def set_sentinel_band_uri_1(self, value):
        self._sentinel_band_uri_1 = value

    def get_sentinel_band_uri_2(self):
        return self._sentinel_band_uri_2

    def set_sentinel_band_uri_2(self, value):
        self._sentinel_band_uri_2 = value

    def get_polygon_path(self):
        return self._polygon_path

    def set_polygon_path(self, value):
        self._polygon_path = value

    def calculate_valid_geometries(self, polygon):
        valid_geometries = []
        for geom in polygon.geometry:
            if not geom.is_empty:
                valid_geometries.append(geom)
        return valid_geometries

    def calculate_band_data(self, sentinel_band_uri_1):
        # Read the polygon from the GeoJSON file
        polygon = gpd.read_file(self.get_polygon_path())

        with rasterio.open(sentinel_band_uri_1) as src:
            # Adjusting the projection of polygon same as sentinel imagery
            polygon = polygon.to_crs(src.crs)

            # identifies and collects valid geometries within the polygon
            valid_geometries = self.calculate_valid_geometries(polygon)

            # Open the sentinel2 satellite using rasterio xarray
            # And chunk the data for efficiency
            sentinel2_band_data = rioxarray.open_rasterio(sentinel_band_uri_1, masked=True).chunk({'x': self.chunk_size[0], 'y': self.chunk_size[0]})

            # Extract the subset of imagery that lies in the valid polygon
            band_subset = sentinel2_band_data.rio.clip(valid_geometries).compute(scheduler='threads')

        return band_subset

    def calculate_ndvi(self):
        self.ndvi_array = (self.band_subset_2 - self.band_subset_1) / (
                    self.band_subset_2 + self.band_subset_1)

    def save_ndvi_png(self):
        # Display the NDVI array as an image
        # squeeze is removing 1 DIMENSION data from the ndvi_array so that it's suitable for showing as image
        plt.imshow(self.ndvi_array.squeeze(), cmap=self.colormap)

        # Add a colorbar to the plot and label it
        plt.colorbar(label=self.png_label)

        plt.title('Normalized Difference Vegetation Index (NDVI)')
        plt.savefig(self.output_ndvi_png)
        plt.show()

    def calculate_and_save(self):
        self.band_subset_1 = self.calculate_band_data(self.get_sentinel_band_uri_1())
        self.band_subset_2 = self.calculate_band_data(self.get_sentinel_band_uri_2())
        self.calculate_ndvi()
        self.save_ndvi_png()
        return self.ndvi_array
