lst = []

for i in range(1, 16):
    lst.append(i)

print(lst)

lst_1 = list(filter(lambda num: num % 2 == 1, lst))
print(lst_1)
square = list(map(lambda num: num ** 2, lst_1))
print(square)
