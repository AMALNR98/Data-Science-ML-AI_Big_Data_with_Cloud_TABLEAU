import numpy as np

matrix_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(matrix_1)
print("*"*50, "1-D matrix", "*"*50)

# sum
sum_of_matrix = np.sum(matrix_1)
print(sum_of_matrix)
print("*"*50, "2-D matrix", "*"*50)
# sum function in 2-d matrix
matrix_2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6], [1, 3, 6, 3]])
print(matrix_2)
sum_of_2_d_matrix = np.sum(matrix_2)
print(sum_of_2_d_matrix)


# axis = 0 ---> columns
# axis = 1 ---> row
print("*"*50, "To find sum of each column of 2-D matrix", "*"*50)
sum_of_each_columns_of_2_d_matrix = np.sum(matrix_2, axis=0)
print(sum_of_each_columns_of_2_d_matrix)

print("*"*50, "To find sum of each row of 2-D matrix", "*"*50)
sum_of_each_rows_of_2_d_matrix = np.sum(matrix_2, axis=1)
print(sum_of_each_rows_of_2_d_matrix)
