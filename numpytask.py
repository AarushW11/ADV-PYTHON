import numpy as np

# Create a NumPy array of temperatures for 10 days
temperatures = np.array([30, 32, 31, 29, 33, 35, 34, 32, 31, 30])

# Display temperatures for the first 3 days
print("Temperatures for first 3 days:", temperatures[:3])

# Display temperatures from day 5 to day 8
print("Temperatures from day 5 to day 8:", temperatures[4:8])

# Calculate average, maximum, minimum and total
print("Average temperature:", np.mean(temperatures))
print("Maximum temperature:", np.max(temperatures))
print("Minimum temperature:", np.min(temperatures))
print("Total temperature:", np.sum(temperatures))

# Increase every temperature by 2°C using broadcasting
modified_temperatures = temperatures + 2

# Display modified array
print("Modified temperatures:", modified_temperatures)
