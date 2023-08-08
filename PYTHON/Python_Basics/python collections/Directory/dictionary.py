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
