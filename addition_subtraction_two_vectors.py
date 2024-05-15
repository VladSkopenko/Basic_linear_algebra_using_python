import numpy as np


a = np.array([1, 2, 3, 4, 5], dtype=float)
print(a.size)  # метод векторов который позволяет узнать размер

a = np.array(
    [1, 2, 3,]
)
b = np.array(
    [4, 5, 6]
)
result = a + b
print(result)
result = a - b
print(result)
# Эти операции возможны только если вектора одинакового размера( что бы это понять есть метод size)
# Addition subtraction  работае так же просто как и простой скаляр  а1 + в1
result = np.dot(a, b)
print(result)
# Скалярний добуток a * b = a1*b1 + a2*b2 + a3*b3 + a4*b4 + a5*b5 + a_n *b_n
