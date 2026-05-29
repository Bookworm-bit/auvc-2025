import numpy as np

# Problem 1
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Problem 1")

print(a + b)
print(a - b)

print()

# Problem 2
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Problem 2")

print(A + B)
print(A - B)

print()

# Problem 3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Problem 3")

print(np.dot(a, b))

print()

# Problem 4
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])

print("Problem 4")

print(A @ B)

print()

# Problem 5
a = np.array([1, 1, 2])

print("Problem 5")

print(np.linalg.norm(a))

print()

# Problem 6
A = np.array([[1, 2], [3, 4]])

print("Problem 6")

print(A.T)
