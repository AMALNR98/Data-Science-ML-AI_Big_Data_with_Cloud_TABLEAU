lst = []

for i in range(1, 101):
    lst.append(i)

print(lst)

lst_1 = list(filter(lambda num: num % 2 == 0, lst))
print(lst_1)
