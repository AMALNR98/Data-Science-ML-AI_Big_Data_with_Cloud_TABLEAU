import numpy as np

a = np.array([[5, 3, 3], [3, 4, 3], [3, 5, 6], [4, 3, 2]])

b = np.where(a == 5)
print(b)

#
c = np.where(a > 4)
print(c)

# confused, check properly

d = np.where(a % 2 == 0)
print(b)

# here
# array[], array[]
# row       column
