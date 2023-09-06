import pandas as pd

# Sample data in dictionary format
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'],
    'Country': ['USA', 'USA', 'USA', 'USA', 'USA'],
    'Latitude': [40.7128, 34.0522, 41.8781, 29.7604, 25.7617],
    'Longitude': [-74.0060, -118.2437, -87.6298, -95.3698, -80.1918]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    city_name = row['City']
    country_name = row['Country']
    latitude = row['Latitude']
    longitude = row['Longitude']
    
    print(f"City: {city_name}")
    print(f"Country: {country_name}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print("\n")
