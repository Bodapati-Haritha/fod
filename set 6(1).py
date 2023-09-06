import pandas as pd
import matplotlib.pyplot as plt

# Load stock data from CSV file
df = pd.read_csv('stock_data.csv')

# Calculate daily price variations
df['Price_Variation'] = df['Closing_Price'].diff()

# Calculate mean, standard deviation, and range
mean_price = df['Closing_Price'].mean()
std_deviation = df['Closing_Price'].std()
price_range = df['Closing_Price'].max() - df['Closing_Price'].min()

# Create line plot for stock prices
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Closing_Price'], label='Closing Price', color='blue')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price Variability Over Time')
plt.xticks(rotation=45)
plt.legend()

# Create line plot for daily price variations
plt.figure(figsize=(12, 4))
plt.plot(df['Date'], df['Price_Variation'], label='Price Variation', color='red')
plt.xlabel('Date')
plt.ylabel('Price Variation')
plt.title('Daily Price Variations')
plt.xticks(rotation=45)
plt.legend()

# Show plots
plt.tight_layout()
plt.show()

# Display statistics
print(f"Mean Price: {mean_price:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")
print(f"Price Range: {price_range:.2f}")
