from Census_data import Census

# Create an instance of the Census class
census_instance = Census()

# Load the CSV files into the class attributes
census_instance.load_data('pivot_Immigrant_status_sum.csv', 'pivot_total_census_families_sum.csv', 'pivot_marital_status_sum.csv')

# Call the census_wrapper method to get the merged DataFrame
census_combined = census_instance.census_wrapper()

# Save the combined DataFrame to a CSV file
# census_combined.to_csv('census_wrapper_combined.csv', sep=',')

# Access and print the merged DataFrame
print(census_combined)
