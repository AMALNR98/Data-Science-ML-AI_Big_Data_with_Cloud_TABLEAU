lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)

# append
lst.append(50)
print(lst)

lst.append(100)
print(lst)

# append takes exactly one argument at time
# lst.append(100, 50, 10) is not possible


# extend : is used to append multiple elements to a list

lst.extend([75, 100, 150, 'bigdata'])
print(lst)
