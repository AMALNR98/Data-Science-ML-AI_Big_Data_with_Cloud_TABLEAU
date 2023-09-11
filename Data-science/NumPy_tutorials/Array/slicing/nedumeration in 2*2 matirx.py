import numpy as np

a = np.array([[3, 4, 5], [5, 1, 9], [5, 9, 7]])
for j,x in np.ndenumerate(a):
    print(j,x)