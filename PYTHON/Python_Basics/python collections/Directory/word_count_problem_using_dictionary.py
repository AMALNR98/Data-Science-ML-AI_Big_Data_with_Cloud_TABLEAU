# Word count problem

# here a string of data is given
line = 'hadoop spark pig hive sqoop hive spark hadoop hive pig spark sqoop'

# we need to split the data
# split()

data = line.split(' ')  # here a list will create
print(data)

# Create an empty dictionary

dictionary_1 = {}
for i in data:
    if i not in dictionary_1:
        dictionary_1[i] = 1
    else:
        dictionary_1[i] += 1
print(dictionary_1)