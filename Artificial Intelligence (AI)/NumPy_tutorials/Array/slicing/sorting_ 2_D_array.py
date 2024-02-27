import numpy as np

print("*" * 50, "2-D matrix sorting", "*" * 50)
matrix_1 = np.array([[1, 6, 7, 4], [9, 3, 6, 7], [1, 4, 5, 6], [1, 3, 6, 3]])
print(matrix_1)

# the matrix sort in row wise
print("*" * 50, "2-D matrix sorted in row wise", "*" * 50)
sorted_matrix = np.sort(matrix_1)
print(sorted_matrix)

print("*" * 50, "2-D matrix sorted in column wise", "*" * 50)
sorted_matrix_column_wise = np.sort(matrix_1, axis=0)
print(sorted_matrix_column_wise)
