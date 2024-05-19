import numpy as np

base_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(base_matrix)
transport_matrix = base_matrix.T
print(f"{'-' * 35}")
print(f"Транспонована матриця, рядки та стовпці змінено місцями")
print(transport_matrix)

