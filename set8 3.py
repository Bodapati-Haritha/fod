import pandas as pd
import matplotlib.pyplot as plt

# Load the temperature data from a CSV file (replace 'temperature_data.csv' with your data file)
data = pd.read_csv('temperature_data.csv')

# Group data by city and calculate mean and standard deviation
city_stats = data.groupby('City')['Temperature'].agg(['mean', 'std']).reset_index()

# Calculate the temperature range (difference between max and min) for each city
city_stats['Range'] = data.groupby('City')['Temperature'].agg(lambda x: x.max() - x.min()).values

# Find the city with the highest temperature range
city_with_highest_range = city_stats.loc[city_stats['Range'].idxmax()]

# Print city with the highest range
print(f"City with the Highest Temperature Range: {city_with_highest_range['City']}")
print(f"Mean Temperature: {city_with_highest_range['mean']:.2f}")
print(f"Standard Deviation: {city_with_highest_range['std']:.2f}")
print(f"Temperature Range: {city_with_highest_range['Range']:.2f}")

# Create a histogram for the city with the highest range
city_data = data[data['City'] == city_with_highest_range['City']]
plt.hist(city_data['Temperature'], bins=20, edgecolor='k')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title(f'Temperature Histogram for {city_with_highest_range["City"]}')
plt.grid(True)
plt.show()
