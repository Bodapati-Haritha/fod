import numpy as np

# Given dataset
data = [5, 8, 10, 12, 15, 18, 20, 25]

# Population size
population_size = len(data)

# Population mean estimation
population_mean = np.mean(data)

# Population variance estimation
population_variance = np.var(data, ddof=0)

# Random sampling from the population (example: sample size = 3)
sample_size = 3
random_sample = np.random.choice(data, size=sample_size, replace=False)

# Display the results
print(f"Population Mean Estimation: {population_mean:.2f}")
print(f"Population Variance Estimation: {population_variance:.2f}")
print(f"Random Sample of Size {sample_size}: {random_sample}")
