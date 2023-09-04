# Zero matrix

# [ 0 0 0 ]
# [ 0 0 0 ] (2*3)

# [0 0]
# [0 0]
# [0 0]     (3*2)

# zeros function is used to create zero matrix
import numpy as np

zero_matrix = np.zeros([3,4])
print(zero_matrix)

# To print datatype of a matrix we use 'dtype'
a = np.array([4, 5, 6, 7])
print(a)
print(a.dtype)

# to convert datatype
b = np.array([4, 5, 6, 7], dtype=float)
print(b)
print(b.dtype)
