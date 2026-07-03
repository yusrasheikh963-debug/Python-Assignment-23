import numpy as np

arr = np.random.randint(10, 101, size=(5, 6))   # Create 2D array of shape (5, 6) with random integers between 10 & 100

print("Array:")   # Print the array
print(arr)

print("\nShape:", arr.shape)    # Print message of the output screen
print("Total number of elements (size):", arr.size)
print("Data type (dtype):", arr.dtype)