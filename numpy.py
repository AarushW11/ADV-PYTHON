import numpy as np

# 1. Create a one-dimensional array containing numbers from 1 to 10
arr = np.arange(1, 11)
print("Original array:", arr)

# 2. Slicing operations
print("First five elements:", arr[:5])
print("Last five elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Every second element:", arr[::2])

# 3. Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Broadcasting
# Add 5 to every element
arr_added = arr + 5
print("After adding 5:", arr_added)

# Multiply every element by 2
arr_multiplied = arr * 2
print("After multiplying by 2:", arr_multiplied)

# Modify selected elements using broadcasting
arr[0:5] += 10
print("After adding 10 to first five elements:", arr)
