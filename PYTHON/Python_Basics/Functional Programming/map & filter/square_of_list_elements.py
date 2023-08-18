lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def square(num):
#     return num ** 2
#
#
# lst_1 = list(map(square, lst))
# print(lst_1)


# replaced by lambda

lst_1 = list(map(lambda num: num ** 2, lst))
print(lst_1)
