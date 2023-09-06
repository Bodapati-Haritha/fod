import pandas as pd

# Create a DataFrame with the provided data
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'CustomerAge': [28, 32, 25, 38, 30, 22, 28, 35, 40, 29],
    'PurchaseAmount': [50, 100, 75, 120, 90, 60, 70, 130, 110, 95]
}

df = pd.DataFrame(data)

# Filter the DataFrame to include only customers who made a purchase
purchased_customers = df[df['PurchaseAmount'] > 0]

# Calculate the frequency distribution of customer ages
age_distribution = purchased_customers['CustomerAge'].value_counts().sort_index()

# Print the frequency distribution
print("Age Frequency Distribution:")
print(age_distribution)
