import numpy as np

a = np.array([[1, 0, 3],
              [-1, -1, 2],
              [4, 7, 2]
              ]
             )

a_inv = np.linalg.inv(a)
print(a_inv)
