# Tuples

# tu = ()  # How to define
# # OR
# tu_1 = tuple()
#
# # support heterogeneous data
# tu = (10, 10.5, 'bigdata', True)
# print(tu)
#
# # insertion node is preserved
# tu_2 = (10, 10.5, 'bigdata', True, 1, 2, 3, 4)
#
# # support duplicate values
# tu_3 = (10, 10, 10, 10.5, 'bigdata', True, 1, 2, 3, 4)
# print(tu_3)

# tuple is immutable
# --------------------
tu_4 = (10, 34, 43, 434, 343, 343, 12)
tu_4[3] = 100 # it's not possible
print(tu_4)
