import pandas as pd

# Sample housing data as a dictionary
data = {
    'HouseID': [1, 2, 3, 4, 5],
    'Price': [300000, 450000, 250000, 600000, 350000],
    'Bedrooms': [3, 4, 2, 5, 3],
    'Bathrooms': [2, 3, 1, 4, 2],
    'SquareFeet': [1800, 2400, 1500, 3200, 2000]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    print(f"HouseID: {row['HouseID']}, Price: ${row['Price']}, Bedrooms: {row['Bedrooms']}, Bathrooms: {row['Bathrooms']}, SquareFeet: {row['SquareFeet']} sq. ft.")

# Alternatively, you can access specific columns using their names
# For example, row['HouseID'], row['Price'], etc.
