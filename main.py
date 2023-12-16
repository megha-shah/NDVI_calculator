
from ndvi.ndvi_calculator import NDVICalculator
from ndvi.ndvi_stats_calculator import NDVIStatsCalculator
import os

# Request unauthenticated and unauthorized access to AWS services
# Needed when we don't want to sign in to the AWS account as we are accessing public AWS resources that don't require authentication
os.environ["AWS_NO_SIGN_REQUEST"] = "YES"


def main():
    # this imagery is for date 05-06-2023 and Kenya region
    sentinel2_s3_uri = 's3://sentinel-cogs/sentinel-s2-l2a-cogs/36/N/YF/2023/6/S2B_36NYF_20230605_0_L2A/'
    polygon_file_path = 'polygon/sample_polygon.geojson'

    # Output file paths
    output_png = 'output_files/output_ndvi.png'
    output_stats_csv = 'output_files/output_stats.csv'

    b04_uri = sentinel2_s3_uri + 'B04.tif'
    b08_uri = sentinel2_s3_uri + 'B08.tif'

    ndvi_calculator = NDVICalculator(b04_uri, b08_uri, polygon_file_path, output_png)
    ndvi_array = ndvi_calculator.calculate_and_save()

    stats_calculator = NDVIStatsCalculator(ndvi_array, output_stats_csv)
    stats_calculator.calculate_ndvi_stats()
    print("Process Finished: Generated output files. Check in output_files directory")


if __name__ == "__main__":
    main()
