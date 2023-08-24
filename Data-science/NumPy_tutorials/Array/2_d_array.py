import numpy as np

# three_by_three = np.array([[2, 4, 6, 7], [1, 2, 3, 4], [2, 4, 5]])
# print(three_by_three)
# print(three_by_three.ndim)

# 2*3 2D ARRAY

two_by_three = np.array([[2, 3, 4], [2, 3, 4]])
print(two_by_three)
print(two_by_three.ndim)

four_by_four_order_three_dimensional = np.array([[[1, 2, 3, 4], [1, 3, 4, 5], [2, 3, 5, 3], [1, 2, 3, 4]]])
print(four_by_four_order_three_dimensional)
print(four_by_four_order_three_dimensional.ndim)

arr1 = np.array([[[2, 17], [45, 78]], [[88, 92], [60, 76]], [[76, 33], [20, 18]]])
print(arr1)

# size ==> total no of elements in array
# 3 rows 3 columns ===> 3*3 ==> 9
# Total no fo elements ==> number of columns * number of rows


# To print order of a matrix
# ---------------------------
# shape
print(two_by_three.shape)