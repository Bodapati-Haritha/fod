import pandas as pd
import matplotlib.pyplot as plt

# Mock dataset
data = {
    'Name': ['Lionel Messi', 'Cristiano Ronaldo', 'Neymar Jr', 'Kylian Mbappe', 'Robert Lewandowski'],
    'Age': [34, 36, 29, 23, 33],
    'Position': ['Forward', 'Forward', 'Forward', 'Forward', 'Forward'],
    'Goals': [40, 38, 30, 28, 36],
    'Salary': [10000000, 9500000, 8000000, 7000000, 8500000]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Find the top 5 players with the highest number of goals scored
top_goals_players = df.nlargest(5, 'Goals')

# Find the top 5 players with the highest salaries
top_salary_players = df.nlargest(5, 'Salary')

# Calculate the average age of players
average_age = df['Age'].mean()

# Display the names of players above the average age
above_average_age_players = df[df['Age'] > average_age]['Name']

# Visualize the distribution of players based on their positions using a bar chart
position_counts = df['Position'].value_counts()
position_counts.plot(kind='bar', title='Player Distribution by Position')
plt.xlabel('Position')
plt.ylabel('Count')
plt.show()

# Print the results
print("Top 5 Players with the Highest Goals:")
print(top_goals_players[['Name', 'Goals']])

print("\nTop 5 Players with the Highest Salaries:")
print(top_salary_players[['Name', 'Salary']])

print(f"\nAverage Age of Players: {average_age:.2f}")

print("\nPlayers Above Average Age:")
print(above_average_age_players)
