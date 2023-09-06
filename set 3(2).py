import pandas as pd
import numpy as np

# Sample dataset (replace with your actual dataset)
data = {
    'City': ['CityA', 'CityA', 'CityA', 'CityB', 'CityB', 'CityB', 'CityC', 'CityC', 'CityC'],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03'],
    'Temperature': [20, 22, 19, 25, 24, 26, 18, 19, 17]
}

# Create a DataFrame from the dataset
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the mean temperature for each city
mean_temperatures = df.groupby('City')['Temperature'].mean()

# Calculate the standard deviation of temperature for each city
std_dev_temperatures = df.groupby('City')['Temperature'].std()

# Determine the city with the highest temperature range
temperature_range = df.groupby('City')['Temperature'].max() - df.groupby('City')['Temperature'].min()
city_with_highest_range = temperature_range.idxmax()
highest_range = temperature_range.max()

# Find the city with the most consistent temperature (lowest standard deviation)
city_with_lowest_std_dev = std_dev_temperatures.idxmin()
lowest_std_dev = std_dev_temperatures.min()

# Print the results
print("Mean Temperature for Each City:")
print(mean_temperatures)

print("\nStandard Deviation of Temperature for Each City:")
print(std_dev_temperatures)

print(f"\nCity with the Highest Temperature Range: {city_with_highest_range} (Range: {highest_range}°C)")

print(f"\nCity with the Most Consistent Temperature: {city_with_lowest_std_dev} (Standard Deviation: {lowest_std_dev:.2f})")
