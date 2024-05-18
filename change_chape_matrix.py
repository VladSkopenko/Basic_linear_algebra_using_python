import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a)
print("Розмірність матриці reshape()")
b = a.reshape((3, 2))
print(b)
print("Матриця плоска flatten()")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.flatten()
print(b)
