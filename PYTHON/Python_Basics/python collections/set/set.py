# 1. how to define
set_0 = {1, 2, 3}
# To define empty set
set_dect_empty = {}  # it's not set, it's defined as dictionary
set_empty = set()
print(type(set_0))
print((type(set_0)))
print(type(set_dect_empty))

# 2. set is heterogeneous?
set_heterogeneous = {10, 10.5, 'bigdata', True}
print(set_heterogeneous)

# 3. insertion order is not preserved

# 4. duplicate values are not supported
set_duplicate = {1, 2, 1, 3, 2, 3}
print(set_duplicate)

# sum of set
set_sum = {1, 2, 3, 5, 4, 6, 45, 45, 45}
print(set_sum)
print(sum(set_sum))

# max value in set
print(max(set_sum))

# min value in set
print(min(set_sum))

# length of set
print(len(set_sum))  # only takes non-duplicate values

# To insert value to set
set_sum.add(7)
set_sum.add(19)
print(set_sum)

# To add multiple values to set
# "update"
set_sum.update([9, 10, 11])
print(set_sum)

# delete element form set
# remove or pop is used
set_sum.remove(11)
print(set_sum)
set_sum.pop()   # When we use pop here one element randomly removed
print(set_sum)