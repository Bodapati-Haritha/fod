import numpy as np
from scipy import stats

# Sample data (replace with your actual data)
design_A = [0.12, 0.1, 0.11, 0.13, 0.14, 0.12, 0.11, 0.13, 0.12, 0.12]
design_B = [0.15, 0.14, 0.16, 0.17, 0.15, 0.16, 0.15, 0.16, 0.17, 0.15]

# Perform the t-test
t_statistic, p_value = stats.ttest_ind(design_A, design_B)

# Set the significance level
alpha = 0.05

# Compare p-value to the significance level
if p_value < alpha:
    print("Reject the null hypothesis: There is a statistically significant difference.")
else:
    print("Fail to reject the null hypothesis: There is no statistically significant difference.")

# Print the test statistics and p-value
print(f"t-statistic: {t_statistic:.2f}")
print(f"p-value: {p_value:.4f}")
