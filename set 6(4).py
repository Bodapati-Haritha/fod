import numpy as np

# Fuel efficiency data for different car models
fuel_efficiency = np.array([25, 30, 22, 28, 35, 18, 32, 24])

# Calculate the average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)

# Calculate the percentage improvement in fuel efficiency between two car models
model1_fuel_efficiency = fuel_efficiency[0]  # Example: Car model 1
model2_fuel_efficiency = fuel_efficiency[1]  # Example: Car model 2

percentage_improvement = ((model2_fuel_efficiency - model1_fuel_efficiency) / model1_fuel_efficiency) * 100

# Display results
print(f"Average Fuel Efficiency: {average_fuel_efficiency:.2f} miles per gallon")
print(f"Percentage Improvement between Model 1 and Model 2: {percentage_improvement:.2f}%")
