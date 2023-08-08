#   Set operations
# Union
# Intersections
# Difference

set_1 = {1, 2, 3, 5, 4, 6, 45, 45, 45}
set_2 = {1, 2, 1, 3, 2, 3}

# Union
set_3 = set_1.union(set_2)
print(set_3)

# Intersection
set_4 = set_1.intersection(set_2)
print(set_4)

# Difference
# A-B -> element presented in A should not present in B
set_5 = set_1.difference(set_2)
print(set_5)

