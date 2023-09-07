import numpy as np

print("*" * 50, "1-D matrix max", "*" * 50)
matrix_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(matrix_1)
max_of_matrix_1 = np.max(matrix_1)
print(max_of_matrix_1)

print("*" * 50, "2-D matrix max", "*" * 50)
matrix_2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6], [1, 3, 6, 3]])
print(matrix_2)
max_of_matrix_2 = np.max(matrix_2)
print(max_of_matrix_2)

print("*" * 50, "2-D matrix max in columns", "*" * 50)
max_of_matrix_2_column = np.max(matrix_2, axis=0)
print(max_of_matrix_2_column)

print("*" * 50, "2-D matrix max in rows", "*" * 50)
max_of_matrix_2_rows = np.max(matrix_2, axis=1)
print(max_of_matrix_2_rows)
