import numpy as np





a = np.array(
    [
        1,
        2,
        3,
    ]
)
b = np.array([1, 2, 3])
print(f"{a.size} Розмір вектора, за допомогою метода size, це кількість елементів")
result = a + b
print(f"{result} Додавання та віднімання векторів, а1 +- в1")
result = a - b
print(result)
# Эти операции возможны только если вектора одинакового размера( что бы это понять есть метод size)
# Addition subtraction  работае так же просто как и простой скаляр  а1 + в1
result = np.dot(a, b)
print(f"{result} Скалярний добуток")
# Скалярний добуток a * b = a1*b1 + a2*b2 + a3*b3 + a4*b4 + a5*b5 + a_n *b_n
print(f"{a.shape} кількість координат вектора ")