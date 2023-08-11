customer = open('/home/amal/Downloads/customer1.txt', 'r')
filtered_dictionary = {}

for i in customer:
    data = i.rstrip('\n').split(',')
    if data[4] == 'Doctor':
        print(data[1:5])