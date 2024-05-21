import numpy as np

first_nature_vector = np.arange(1, 11)
print(f"1.Одновимірний масив  з першими 10-ма натуральними:\n{first_nature_vector}")

matrix_zero = np.zeros((3, 3))
print(f"2.Матриця 3х3 заповнена нулями:\n{matrix_zero}")

matrix_5x5 = np.random.randint(1, 11, size=(5, 5))
print(f"3.Матриця 5х5 заповнена випадковими числами від 1 до 10:\n{matrix_5x5}")

array_4x4 = np.random.rand(4, 4)
print(f"4.Матриця розміром 4x4 з випадковими дійсними числами від 0 до 1:{array_4x4}")


vector_1 = np.random.randint(1, 11, size=(5,))
vector_2 = np.random.randint(1, 11, size=(5,))
sum_vectors = vector_1 + vector_2
minus_vectors = vector_1 - vector_2
product_vectors = vector_1 * vector_2
print(
    "5.Сума, різниця, добуток векторів:\n",
    sum_vectors,
    "\n",
    minus_vectors,
    "\n",
    product_vectors,
)

vector_1 = np.random.randint(1, 11, size=(7,))
vector_2 = np.random.randint(1, 11, size=(7,))
scalar_product = np.dot(vector_1, vector_2)
print("6.Скалярний добуток векторів:\n", scalar_product)

matrix_1 = np.random.randint(1, 11, size=(2, 2))
matrix_2 = np.random.randint(1, 11, size=(2, 3))
matrix_product = np.dot(matrix_1, matrix_2)
print("7.Добуток матриць:\n", matrix_product)

base_matrix = np.random.randint(1, 11, size=(3, 3))
inverse_matrix = np.linalg.inv(base_matrix)
print("8.Обернена матриця:\n", inverse_matrix)

base_matrix = np.random.rand(4, 4)
transport_matrix = base_matrix.T
print("9.Транспонована матриця:\n", transport_matrix)

matrix = np.random.randint(1, 11, size=(3, 4))
vector = np.random.randint(1, 11, size=(4,))
result = np.dot(matrix, vector)
print("10.Результат множення матриці на вектор:\n", result)

matrix = np.random.rand(2, 3)
vector = np.random.rand(
    3,
)
result = np.dot(matrix, vector)
print("11.Результат множення матриці на вектор з дійсними числами:\n", result)

matrix_1 = np.random.randint(1, 11, size=(3, 3))
matrix_2 = np.random.randint(1, 11, size=(3, 3))
result = matrix_1 * matrix_2
print("12.Результат  поелементного  множення матриць:\n", result)

matrix_1 = np.random.randint(1, 11, size=(3, 3))
matrix_2 = np.random.randint(1, 11, size=(3, 3))
result = np.dot(matrix_1, matrix_2)
print("13.Добуток матриць:\n", result)

matrix = np.random.randint(1, 101, size=(5, 5))
result = np.sum(matrix)
print("14.Сума елементів матриці:\n", result)

matrix_1 = np.random.randint(1, 11, size=(4, 4))
matrix_2 = np.random.randint(1, 11, size=(4, 4))
result = matrix_1 - matrix_2
print("15.Різниця матриць:\n", result)

matrix = np.random.rand(3, 3)

row_sums = np.sum(matrix, axis=1)
vector_column = row_sums.reshape(-1, 1)
print("16.Сума елементів  кожного рядка матриці:\n", vector_column)

base_matrix = np.random.randint(1, 20, size=(3, 4))
squared_matrix = np.power(base_matrix, 2)
print("17.Квадрат матриці:\n", squared_matrix)

base_vector = np.random.randint(1, 50, size=(4,))
new_vector = np.power(base_vector, 0.5)
print("18.Вектор з квадратними коренями:\n", new_vector)
