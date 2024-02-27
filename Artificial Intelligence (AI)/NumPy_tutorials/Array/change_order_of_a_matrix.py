# 2-d 4*3 matrix
import numpy as np

matrix_1 = np.array([[4, 5, 6], [5, 6, 4], [3, 4, 5], [4, 5, 6]])
print(matrix_1)
# to change order of a matrix use reshape
print("*" * 100)

reshaped_matrix = matrix_1.reshape([3, 4])
print(reshaped_matrix)

# here [3*3] is not possible
# [3,5] is not possible
# the total number of elements should be equal
