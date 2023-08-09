# Dictionary
# It's a key value pair
# 1. How to define

dictionary_empty = {}
"""
key value pair  
id : 101
first_name : vinay
last_name : k
age : 28
prof : bigdata
"""

dictionary_example = {'id': 101, 'first_name': 'vinay', 'last-name': 'b', 'age': 28, 'prof': 'bigdata'}
print(dictionary_example)

# it support heterogeneous data

# Insertion order is preserved

# duplicate key is not supported
dictionary_duplicate_key = {'id': 101, 'first_name': 'vinay', 'last-name': 'b', 'age': 28, 'prof': 'bigdata', 'age': 30}
print(dictionary_duplicate_key)

# dictionary supports duplicate values
dictionary_duplicate_value = {'id': 101, 'first_name': 'vinay', 'last-name': 'vinay', 'prof': 'bigdata', 'age': 30}
print(dictionary_duplicate_value)

# dictionary is mutable


# To collect a particular value using it's corresponding value
print("To collect a particular value using it's corresponding value")
print(dictionary_duplicate_value['age'])
print(dictionary_duplicate_value['first_name'], "\n")

# To print key value pair
for i in dictionary_duplicate_value:
    print(i, ",", dictionary_duplicate_value[i], "\n")

# How to update value
print("How to update a value in dictionary")
dictionary_duplicate_value['age'] = 30
print(dictionary_duplicate_value, "\n")

# add value in age
dictionary_duplicate_value['age'] += 10
print(dictionary_duplicate_value, '\n')

# add new key-value pair
print("Add new key-value pair")
dictionary_duplicate_value['total'] = 75
print(dictionary_duplicate_value, "\n")

#
