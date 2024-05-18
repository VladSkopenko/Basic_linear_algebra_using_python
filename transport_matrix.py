import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a)
b = a.T
print(f"{'-' * 35}")
print(f"Транспонована матриця, рядки та стовпці змінено місцями")
print(b)

