# empty list
# 1 - 100 element
# even list
# odd list
# 3 list display

lst = []
list_even = []
list_odd = []
for i in range(1, 101):
    lst.append(i)

for i in lst:
    if i % 2 ==0:
        list_even.append(i)
    else:
        list_odd.append(i)

print(lst)
print(list_odd)
print(list_even)
print(sum(list_odd))
print(sum(list_even))