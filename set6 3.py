import numpy as np

# Sales data for each quarter
sales_data = np.array([500000, 600000, 700000, 800000])

# Calculate the total sales for the year
total_sales = np.sum(sales_data)

# Calculate the percentage increase from the first quarter to the fourth quarter
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

# Print the results
print(f"Total Sales for the Year: ${total_sales}")
print(f"Percentage Increase from Q1 to Q4: {percentage_increase:.2f}%")
