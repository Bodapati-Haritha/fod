import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the car data into a DataFrame
data = {
    'Car_Model': ['Sedan', 'SUV', 'Hatchback', 'Convertible'],
    'Engine_Size': [2.0, 3.5, 1.4, 2.5],
    'Horse_Power': [150, 280, 100, 200],
    'Fuel_efficiency': [30, 20, 40, 25],
    'Age': [3, 2, 1, 2],
    'Price': [25000, 40000, 16000, 30000]
}

df = pd.DataFrame(data)

# Features (engine size, horsepower, fuel efficiency, age)
X = df[['Engine_Size', 'Horse_Power', 'Fuel_efficiency', 'Age']]

# Target variable (price)
y = df['Price']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the model's coefficients and performance metrics
print("Model Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")

print(f"\nMean Squared Error: {mse:.2f}")
print(f"R-squared (R2) Score: {r2:.2f}")

# Create a scatter plot to visualize actual vs. predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs. Predicted Car Prices")
plt.grid(True)
plt.show()
