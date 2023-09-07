import numpy as np

print("*" * 50, "1-D matrix arg-sort", "*" * 50)
matrix_1 = np.array([1, 4, 2, 7, 9, 3, 11, 4, 3, 5, 11, 6, 43, 7, 1, 8, 7, 9])
print(matrix_1)

# Returns the indices that would sort an array.
# Perform an indirect sort along the given axis using the algorithm specified by the kind keyword
arg_sort_matrix = np.argsort(matrix_1)
print(arg_sort_matrix)

