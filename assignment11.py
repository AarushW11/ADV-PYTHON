import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
data = pd.Series(np.random.randint(1, 100, 10))

# Display the Series
print("Original Series:")
print(data)

# Indexing
print("\nElement at index 2:", data[2])

# Filtering
print("\nNumbers greater than 50:")
print(data[data > 50])

# Statistical operations
print("\nMean:", data.mean())
print("Median:", data.median())
print("Minimum:", data.min())
print("Maximum:", data.max())
