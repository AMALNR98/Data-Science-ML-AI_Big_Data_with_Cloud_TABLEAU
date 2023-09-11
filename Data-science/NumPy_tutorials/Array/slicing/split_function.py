# split

import numpy as np

a = np.array([5, 3, 5, 3, 3, 4, 3, 2])

b = np.array_split(a, 3)
print(b)

