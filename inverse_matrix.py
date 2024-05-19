import numpy as np
matrix_base = np.array([[1, 0, 3],
              [-1, -1, 2],
              [4, 7, 2]
              ]
             )

inverse_matrix = np.linalg.inv(matrix_base)
print(inverse_matrix)
result = np.dot(matrix_base, inverse_matrix)
print(result)
