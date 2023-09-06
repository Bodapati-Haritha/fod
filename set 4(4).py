import pandas as pd

# Given Series 1 and Series 2
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([5, 15, 25, 35, 45])

# Combine the two series into a DataFrame
df = pd.DataFrame({'Series 1': series1, 'Series 2': series2})

# Display the resulting DataFrame
print(df)
