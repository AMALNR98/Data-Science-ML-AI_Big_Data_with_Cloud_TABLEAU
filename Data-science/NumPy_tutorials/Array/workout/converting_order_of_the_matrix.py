# 4*5 ====> [5,4], [10,2] ====> one-dimensional

import numpy as np

matrix_1 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]])
print(matrix_1)
matrix_5_by_4 = matrix_1.reshape([5,4])
print(matrix_5_by_4)
matrix_10_by_2 = matrix_1.reshape([10,2])
print(matrix_10_by_2)