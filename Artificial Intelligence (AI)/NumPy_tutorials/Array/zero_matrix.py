# Zero matrix

# [ 0 0 0 ]
# [ 0 0 0 ] (2*3)

# [0 0]
# [0 0]
# [0 0]     (3*2)

# zeros function is used to create zero matrix
import numpy as np

zero_matrix = np.zeros([3, 4])
print(zero_matrix.dtype)
print(zero_matrix)

# To print datatype of a matrix we use 'dtype'
a = np.array([4, 5, 6, 7])
print(a)
print(a.dtype)

# to convert datatype
b = np.array([4, 5, 6, 7], dtype=float)
print(b)
print(b.dtype)

# in zero matrix the data type is float by default

# 2 *2 zero matrix
two_by_two = np.zeros([2, 2], dtype=int)
print(two_by_two)

# 3 D ===> 4 * 3
three_d_two_by_two = np.zeros([1, 4, 3])
print(three_d_two_by_two)
print(three_d_two_by_two.ndim)
print(three_d_two_by_two.shape)

# 1 D ===> 10 zeros
c = np.zeros([10], dtype=int)
print(c)
print(c.ndim)
print(c.shape)

d = np.zeros([3, 4, 5], dtype=int)
print(d)
print(d.ndim)
print(d.shape)
print(d.size)  # 60 (4*3*5)
