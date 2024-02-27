import numpy as np

a = np.array([[3, 4, 5, 3], [3, 4, 5, 2], [1, 2, 3, 4]])

b = np.array_split(a, 3)
print(b)
