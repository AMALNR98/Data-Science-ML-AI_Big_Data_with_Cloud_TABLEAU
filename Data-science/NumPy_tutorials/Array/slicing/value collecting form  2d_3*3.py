import numpy as np

a = np.array([[3, 4, 5], [5, 1, 9], [5, 9, 7]])
print(a)

for i in a:
    # print(i)
    for j in i:
        print(j)
