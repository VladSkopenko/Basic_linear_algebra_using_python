import numpy as np

matrix_1 = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix_1)
print("Розмірність матриці reshape()")
b = matrix_1.reshape((3, 2))
print(b)
print("Матриця плоска flatten()")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.flatten()
print(b)
