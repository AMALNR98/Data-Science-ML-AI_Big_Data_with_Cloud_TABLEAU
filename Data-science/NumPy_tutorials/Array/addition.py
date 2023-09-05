import numpy as np
# Addition element by element

matrix_1 = np.array([[4, 5, 6], [4, 3, 2], [6, 4, 3]])
matrix_2 = np.array([[4, 5, 6], [4, 3, 2], [6, 4, 3]])
print(matrix_1)
print("*"*100)
print(matrix_2)
print(("*"*100))

sum_of_matrices = np.add(matrix_1, matrix_2)
print(sum_of_matrices)