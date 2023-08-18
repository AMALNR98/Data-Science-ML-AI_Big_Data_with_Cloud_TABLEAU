lst = []

for i in range(1,51):
    lst.append(i)

print(lst)
lst_1 = list(map(lambda num: num + 5, lst))
print(lst_1)