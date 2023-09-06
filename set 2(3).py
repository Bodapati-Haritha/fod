import pandas as pd
import numpy as np
import scipy.stats as stats

# Sample dataset
data = {
    'product_title': ['Pineapple slicer', 'Levis Jeans Pant', 'Wallet', 'Salwar'],
    'product_category': ['Apparel', 'Apparel', 'Apparel', 'Apparel'],
    'star_rating': [4, 5, 5, 5],
    'review_headline': ['Really good', 'Perfect Dress', 'Love it', 'Awesome'],
    'review_date': ['2013-01-14', '2014-04-22', '2015-07-28', '2015-06-12']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Specify the product category to analyze
product_category_to_analyze = 'Apparel'

# Filter the DataFrame for the specified category
category_reviews = df[df['product_category'] == product_category_to_analyze]

# Calculate average rating and standard deviation
average_rating = category_reviews['star_rating'].mean()
std_deviation = category_reviews['star_rating'].std()

# Calculate the confidence interval (95%)
confidence_level = 0.95
n = len(category_reviews)
margin_of_error = stats.t.ppf((1 + confidence_level) / 2, df=n - 1) * (std_deviation / np.sqrt(n))
confidence_interval = (average_rating - margin_of_error, average_rating + margin_of_error)

# Print the results
print(f"Average Rating for {product_category_to_analyze}: {average_rating:.2f}")
print(f"Confidence Interval (95%): ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
