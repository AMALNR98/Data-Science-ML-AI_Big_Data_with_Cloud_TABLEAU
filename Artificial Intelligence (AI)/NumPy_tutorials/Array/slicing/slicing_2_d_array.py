import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]])
print(a)

#  [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9, 10, 11, 12],
#  [13, 14, 15, 16],
#  [17,18,19,20])
# [row, columns]

print(a[:2, :3])  # row =  0,1      columns = 0, 1, 2
# [[1 2 3]
#  [5 6 7]]
print("*" * 100)
print(a[1:4, :2])  # row = 1, 2, 3   columns = 0, 1
# [[ 5  6]
#  [ 9 10]
#  [13 14]]
print("*" * 100)

print(a[1:4, 1:3])  # row = 1, 2, 3 column = 1, 2
# [[ 6  7]
#  [10 11]
#  [14 15]]

print("*" * 100)
print(a[::2, 1:4:2])  # row : 0,2,4    col = 1,3
# [[ 2  4]
#  [10 12]
#  [18 20]]
print("*" * 100)

print(a[1::3, ::2])  # row = 1,4 column = 0,2,
# [[ 5  7]
#  [17 19]]


# 1)  print Zeroth row of data
print("*" * 100)
print(a[0])
#or
print(a[:1,::])
print("*" * 100)

# 2)  print Zeroth column of data
print(a[::,:1])