import pandas as pd

class Census:
    def __init__(self):
        # Initialize empty DataFrames as attributes
        self.pivot_Immigrant_status_sum = pd.DataFrame()
        self.pivot_total_census_families_sum = pd.DataFrame()
        self.pivot_marital_status_sum = pd.DataFrame()

    def load_data(self, immigrant_file, census_families_file, marital_status_file):
        # Load the DataFrames from CSV files into the class attributes
        self.pivot_Immigrant_status_sum = pd.read_csv(immigrant_file, sep=',')
        self.pivot_total_census_families_sum = pd.read_csv(census_families_file, sep=',')
        self.pivot_marital_status_sum = pd.read_csv(marital_status_file, sep=',')

    def census_wrapper(self):
        # Merge the DataFrames on 'GEO_NAME' column
        census_combined = pd.merge(self.pivot_Immigrant_status_sum, self.pivot_total_census_families_sum, on='GEO_NAME')
        census_combined = pd.merge(census_combined, self.pivot_marital_status_sum, on='GEO_NAME')

        return census_combined




