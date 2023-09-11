import numpy as np

a = np.array([4, 5, 3, 5, 2, 7, 8, 9, 10])
for idx,x in np.ndenumerate(a):
    print(idx, x)

