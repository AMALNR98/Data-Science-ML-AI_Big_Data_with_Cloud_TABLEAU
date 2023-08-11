f = open('sample_numbers', 'r')
list_1 = []
for i in f:
    list_1.append(i)

print(list_1)
print(sum(list_1))