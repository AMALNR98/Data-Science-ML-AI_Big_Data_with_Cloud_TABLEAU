# identity matrix

# [1 0 0]
# [0 1 0]
# [0 0 1]

# must be square matrix

# identity
import numpy as np

identity_matrix = np.identity(4, dtype=int)
print(identity_matrix)

# eye function for identity matrix
eye_matrix = np.eye(3, dtype=int)
print(eye_matrix)
 