# Tuples

tu = ()  # How to define
# OR
tu_1 = tuple()

# support heterogeneous data
tu = (10, 10.5, 'bigdata', True)
print(tu)

# insertion node is preserved
tu_2 = (10, 10.5, 'bigdata', True, 1, 2, 3, 4)

# support duplicate values
tu_3 = (10, 10, 10, 10.5, 'bigdata', True, 1, 2, 3, 4)
print(tu_3)

# tuple is immutable
# -------------------
