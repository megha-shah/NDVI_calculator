import numpy as np
import csv


class NDVIStatsCalculator:
    def __init__(self, ndvi_array, output_stats_csv):
        self.ndvi_array = ndvi_array
        self.ndvi_mean = None
        self.ndvi_min = None
        self.ndvi_max = None
        self.output_stats_csv = output_stats_csv

    def calculate_ndvi_stats(self):
        self.ndvi_mean = np.nanmean(self.ndvi_array)
        self.ndvi_min = np.nanmin(self.ndvi_array)
        self.ndvi_max = np.nanmax(self.ndvi_array)
        self.save_ndvi_stats_to_csv_file()

    def save_ndvi_stats_to_csv_file(self):
        with open(self.output_stats_csv, 'w', newline='') as csvfile:
            fieldnames = ['Statistic', 'Value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Statistic': 'Mean NDVI', 'Value': self.ndvi_mean})
            writer.writerow({'Statistic': 'Minimum NDVI', 'Value': self.ndvi_min})
            writer.writerow({'Statistic': 'Maximum NDVI', 'Value': self.ndvi_max})

