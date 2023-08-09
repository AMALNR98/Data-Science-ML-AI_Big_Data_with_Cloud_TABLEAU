# print first recursive character

pattern = 'ABCDEFGHIAJKLMNOPQRSTUVWXYZ'
dictionary_pattern = {}
for i in pattern:
    if i not in pattern:
        pattern_dictionary = 1
    else:
        print("First recursive pattern is :", i)
        break
