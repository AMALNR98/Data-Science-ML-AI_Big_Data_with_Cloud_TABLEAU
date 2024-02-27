# floor , ceil, round

# 4*4

import numpy as np

matrix_1 = np.array([[1.1, 2.2, 3.4, 4.5], [5.4, 6.2, 7.4, 8.08], [9.002, 10.3, 11.2, 12.4], [13.5, 14.1, 15.2, 16.4]])
print(matrix_1)
print("*" * 100)
# [1.1, 2.2, 3.4, 4.5]
# [5.4, 6.2, 7.4, 8.2]
# [9.4, 10.1, 11.2, 12.4]
# [13.5, 14.1, 15.2, 16.4]

# Floor -> will remove the decimal value
matrix_floor = np.floor(matrix_1)
print(matrix_floor)
print("*" * 100)

# ceil
matrix_ceil = np.ceil(matrix_1)
print(matrix_ceil)
print("*" * 100)
# round
matrix_round = np.round(matrix_1)
print(matrix_round)

# --------------------------------------------------------------------------------------------------------------
# for .5 if the number is even the output will be same ,if the number is odd the number will map to next integer
# --------------------------------------------------------------------------------------------------------------
