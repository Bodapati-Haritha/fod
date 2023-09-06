import numpy as np

# Quarterly sales data
sales_data = np.array([500000, 600000, 700000, 800000])

# Calculate total sales for the year
total_sales = np.sum(sales_data)

# Calculate percentage increase from the first quarter to the fourth quarter
first_quarter_sales = sales_data[0]
fourth_quarter_sales = sales_data[-1]

percentage_increase = ((fourth_quarter_sales - first_quarter_sales) / first_quarter_sales) * 100

# Display results
print(f"Total Sales for the Year: ${total_sales}")
print(f"Percentage Increase from Q1 to Q4: {percentage_increase:.2f}%")
