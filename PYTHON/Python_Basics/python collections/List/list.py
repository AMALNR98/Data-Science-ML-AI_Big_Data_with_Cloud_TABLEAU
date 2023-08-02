# Collection
# List

# 1. Define a collection
# Method one
lst = []  # Empty list
print(type(lst))
print(lst)

# Other method using function
lst_1 = list([])
print(type(lst_1))

lst_2 = [1, 2, 3]
print(lst_2)
lst_3 = list([1, 2, 3])
print(lst_3)

# 2. Heterogeneous data
lst_4 = [10, 10.5, 10.555555555555555555555, 123456789, 'bigdata', True]
print(lst_4)

# 3. Duplicates are allowed or not
lst_5 = [10, 10, 10, 'bigdata', 10.5, 10.5, 20, 20]
print(lst_5)
lst_6 = list([10, 10, 'bigdata', 10.4, 10.4])
print(lst_6)

# 4. insertion order preserved.
lst_7 = [1, 2, 3, 4, 5]
print(lst_7)

# 5. list mutable
# list is mutable
