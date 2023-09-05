import numpy as np
matrix_1 = np.array([[4, 5, 6], [4, 3, 2], [6, 4, 3]])
matrix_2 = np.array([[1, 5, 4], [4, 5, 2], [6, 7, 3]])
print(matrix_1)
print("*" * 100)
print(matrix_2)
print(("*" * 100))

difference_of_matrices = np.subtract(matrix_1, matrix_2)
print(difference_of_matrices)
