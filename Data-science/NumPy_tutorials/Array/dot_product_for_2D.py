import numpy as np

matrix_1 = np.array([[4, 5, 6], [4, 3, 2], [6, 4, 3]])
matrix_2 = np.array([[4, 5, 6], [4, 3, 2], [6, 4, 3]])

dot_product = np.dot(matrix_1, matrix_2)
print(dot_product)

# first matrix's number of row and second matrix's number of columns should be equal
