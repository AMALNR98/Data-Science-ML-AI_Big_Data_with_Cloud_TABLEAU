# 5 to 50 [5,10,15,20,..50] --> (5*2)
import numpy as np

matrix_1 = np.arange(5, 51, 5).reshape([5, 2])
print(matrix_1)

# 1 to 20 odd numbers ==> 5*2
matrix_2 = np.arange(1, 20, 2).reshape([5, 2])
print(matrix_2)
