import numpy as np

a = np.array([4.3, 3, 4, 5, 6, 4, 3, 2, 2, 3])
print(a)

print(a[2])
print(a[1:4])
print(a[3:7])

print(a[:6])

print(a[1:])  # index = 1 to end of list
print(a[:])  # complete
print(a[1:5:2])

print(a[::3])  # 0,3,6,9
