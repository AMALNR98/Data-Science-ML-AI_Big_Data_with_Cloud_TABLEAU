# Method 3

# [print_1 if condition_1 if else print_2 range]

# in method 3 there is no "elif" condition

# for multiple conditions
# [print_1 if condition_1 else print_2 if condition_2 else print_3 if condition_3 ....... else print_n range]

#
#
# Examples
# -----------------------------

# 1 to 50 even ===> square
#          odd ===> cube

lst = [(i, i ** 2) if i % 2 == 0 else (i, i ** 3) for i in range(1, 51)]
print(lst)
