import numpy as np

new_vector = np.arange(5)
new_hard_vector = np.arange(start=1, stop=3, step=0.5)
print("метод arange() генерирует массив как обычный ренж ")
print(new_vector)
print(new_hard_vector)


line_space_generator = np.linspace(1, 5, num=20)
line_space_generator2 = np.linspace(1, 5, num=3)
print(line_space_generator)
print(line_space_generator2)
