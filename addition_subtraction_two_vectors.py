import numpy as np


vector_1 = np.array(
    [
        1,
        2,
        3,
    ]
)
vector_2 = np.array([1, 2, 3])
print(
    f"{vector_1.size} Розмір вектора, за допомогою метода size, це кількість елементів"
)
result = vector_1 + vector_2
print(f"{result} Додавання та віднімання векторів, а1 +- в1")
result = vector_1 - vector_2
print(result)
# Эти операции возможны только если вектора одинакового размера( что бы это понять есть метод size)
# Addition subtraction  работае так же просто как и простой скаляр  а1 + в1
result = np.dot(vector_1, vector_2)
print(f"{result} Скалярний добуток")
# Скалярний добуток a * b = a1*b1 + a2*b2 + a3*b3 + a4*b4 + a5*b5 + a_n *b_n
print(f"{vector_1.shape} кількість координат вектора ")
