import pandas as pd

# Sample dataset with likes data
data = {
    'Post_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Likes': [100, 250, 50, 300, 150, 200, 75, 50, 400, 300]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Calculate the frequency distribution of likes
like_distribution = df['Likes'].value_counts().reset_index()
like_distribution.columns = ['Likes', 'Frequency']

# Sort the distribution by the number of likes (optional)
like_distribution = like_distribution.sort_values(by='Likes')

# Print the frequency distribution
print(like_distribution)
