# one matrix
# all elements are one

# [1 1 1]
# [1 1 1]   (2*3)

# [1 1]
# [1 1]
# [1 1] (3*2)

import numpy as np
one_matrix = np.ones([3, 4], dtype=int)
print(one_matrix)
print(one_matrix.shape)
print(one_matrix.ndim)

# one matrix in 3 D

three_d_one = np.ones([1, 3, 4],dtype=int)
print(one_matrix)