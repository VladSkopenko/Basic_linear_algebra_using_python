import numpy as np

object_matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)

# Створення матриці  - це массив з массивами.
# .shape  показує розмірність матриці
# first =  кількість рядків
# second = кількість стовпців

first_value, second_value = object_matrix.shape

print(f"{first_value} - кількість рядків(m)\n{second_value} - кількість стопців(n)")
print(object_matrix.size)

matrix_1= np.array([[1, 2, 3],
              [0, 1, 2]])

matrix_2 = np.array([[1, 2],
              [0, 4],
              [-1, 0]])


c = np.dot(matrix_1, matrix_2)
print(c)
