import numpy as np

a = np.array((35, 34, 23, 35, 36, 39))

b = a > 34

c = a[b]
print(b)
print(c)