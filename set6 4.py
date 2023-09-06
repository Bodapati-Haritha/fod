import numpy as np

# Fuel efficiency data for different car models
fuel_efficiency = np.array([25, 30, 22, 28, 35, 18, 32, 24])

# Calculate the average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)

# Calculate the percentage improvement in fuel efficiency between two car models
model_1_efficiency = fuel_efficiency[0]
model_2_efficiency = fuel_efficiency[4]  # For example, comparing model 1 and model 5

percentage_improvement = ((model_2_efficiency - model_1_efficiency) / model_1_efficiency) * 100

# Print the results
print(f"Average Fuel Efficiency: {average_fuel_efficiency:.2f} miles per gallon")
print(f"Percentage Improvement from Model 1 to Model 5: {percentage_improvement:.2f}%")
