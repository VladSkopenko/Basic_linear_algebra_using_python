import numpy as np

print(
    "Identity matrix - матриця ідентичності, створюється методом eye а параметр k це діагональне зміщення"
)
identity_matrix = np.eye(3, k=0, dtype=float)
print(identity_matrix)


if __name__ == "__main__":
    ...
