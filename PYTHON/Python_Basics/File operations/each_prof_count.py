customer = open('/home/amal/Downloads/customer1.txt', 'r')
filtered_dictionary = {}
prof_list = []

for i in customer:
    data = i.rstrip('\n').split(',')
    prof = data[-2]
    prof_list.append(prof)

for element in prof_list:
    if element not in filtered_dictionary:
        filtered_dictionary[element] = 1
    else:
        filtered_dictionary[element] += 1
    # print(dictionary_1)
# print(prof_list)
for k, v in filtered_dictionary.items():
    print(k, ",", v)
