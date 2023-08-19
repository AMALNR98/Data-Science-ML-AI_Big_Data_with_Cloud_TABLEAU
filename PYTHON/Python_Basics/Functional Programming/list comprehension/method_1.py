# lst = []
# for i in range (1,51):
#     lst.append(i)
# print(lst)
#

# Method 1
# [printing range]

# printing 1 to 30 element in list
lst_1 = [i for i in range(1, 31)]
print(lst_1)

# printing 1 to 51 elements in list
lst_2 = [i for i in range(1, 51)]
print(lst_2)

# printing square of form range 1 to 20
lst_3 = [(i, i ** 2) for i in range(1, 21)]
print(lst_3)

# 1 -30 range ===> cube
lst_4 = [(i, i ** 3) for i in range(1, 30)]
print(lst_4)
