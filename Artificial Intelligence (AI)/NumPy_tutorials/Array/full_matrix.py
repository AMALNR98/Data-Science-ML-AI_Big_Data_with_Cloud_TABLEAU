# full matrix

# value
# [4 4 4]
# [4 4 4]   (2*3)

# [ 6 6 6 6 ]
# [ 6 6 6 6 ]
# [ 6 6 6 6 ] (3*4)

import numpy as np
full_matrix = np.full([3,4], 6)
print(full_matrix)

three_d_full_matrix = np.full([1,2,4], 5)
print(three_d_full_matrix)