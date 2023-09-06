import pandas as pd
import numpy as np

# Read stock data from a CSV file (replace 'stock_data.csv' with your file path)
df = pd.read_csv('stock_data.csv')

# Calculate daily returns as percentage change
df['Daily_Return'] = df['Close'].pct_change() * 100

# Calculate mean daily return and standard deviation of daily returns
mean_return = df['Daily_Return'].mean()
std_deviation = df['Daily_Return'].std()

# Calculate annualized mean return and annualized volatility
annual_mean_return = mean_return * 252  # Assuming 252 trading days in a year
annual_std_deviation = std_deviation * np.sqrt(252)  # Annualized volatility

# Print the results
print(f"Mean Daily Return: {mean_return:.2f}%")
print(f"Standard Deviation of Daily Returns: {std_deviation:.2f}%")
print(f"Annualized Mean Return: {annual_mean_return:.2f}%")
print(f"Annualized Volatility (Standard Deviation): {annual_std_deviation:.2f}%")
