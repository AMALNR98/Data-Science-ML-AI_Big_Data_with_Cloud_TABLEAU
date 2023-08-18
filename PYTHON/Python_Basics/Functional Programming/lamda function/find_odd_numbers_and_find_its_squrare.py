lst = []

for i in range(1, 16):
    lst.append(i)

print(lst)

lst_1 = list(filter(lambda num: num % 2 != 0, lst))
lst_1 = list(map(lambda num: num ** 2, lst_1))
print(lst_1)
