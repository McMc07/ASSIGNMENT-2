import numpy as np

# Dot method
value1 = np.array([[1, 2], [3, 4]])
value2 = np.array([[5, 6], [7, 8]])
total = np.dot(value1, value2)
print("Dot product of 1 and 2:")
print(total)

# Transpose method
sample1 = np.array([[1, 2, 3], [4, 5, 6]])
result = np.transpose(sample1)
print("Transpose of sample1:")
print(result)

# Linalg.inv method
Ex1 = np.array([[1, 2], [3, 4]])
inv_Ex1 = np.linalg.inv(Ex1)
print("Inverse of Ex1:")
print(inv_Ex1)

# Linalg.det method
det_Ex1 = np.linalg.det(Ex1)
print("Determinant of Ex1:", det_Ex1)

# Flatten method
example = np.array([[1, 2], [3, 4]])
flat_example = example.flatten()
print("Flattened example:")
print(flat_example)