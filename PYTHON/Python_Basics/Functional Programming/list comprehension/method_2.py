# Method 2
# [Printing range if condition]

# 1 - 30 range, even
lst = [i for i in range(1, 31) if i % 2 == 0]
print(lst)

# 1 to 50 range, odd number
lst_2 = [i for i in range(1, 51) if i % 2 == 1]
print(lst_2)

# 1 to 50 range, divisible by 5
lst_3 = [i for i in range(1,51) if i % 5 == 0]
print(lst_3)

