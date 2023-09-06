import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Read the stock data from a CSV file (replace 'stock_data.csv' with your file)
data = pd.read_csv('stock_data.csv')

# Assuming you have a 'Date' column in your dataset
data['Date'] = pd.to_datetime(data['Date'])

# Step 3: Calculate the variability (standard deviation) of stock prices
stock_std_dev = data['ClosingPrice'].std()
stock_mean = data['ClosingPrice'].mean()

# Step 4: Visualize stock price movements using a line chart
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['ClosingPrice'], label='Stock Closing Price', color='b')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price Movement')
plt.legend()
plt.grid(True)

# Optionally, you can add insights based on the calculated standard deviation
plt.axhline(stock_mean + stock_std_dev, color='r', linestyle='--', label='1 Std Dev Above Mean')
plt.axhline(stock_mean - stock_std_dev, color='g', linestyle='--', label='1 Std Dev Below Mean')

plt.legend()

# Show the plot
plt.show()
