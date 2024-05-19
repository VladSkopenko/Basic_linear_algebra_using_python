import numpy as np

vector = np.array([1, 2, 3, 4, 5])
vector[0] = 5
print(vector[0])
print(vector[1:])
print(vector[:2])
print("Дефолтний слайс и индексы как в листах")


matrix = np.array([
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9]]) # 2
    #0  1  2
print(matrix[1, 1]) # 5
print(matrix[1:, 1]) # [5, 8]
print(matrix[0, :2]) # [1, 2]
