customer = open('/home/amal/Downloads/customer1.txt', 'r')


for i in customer:
    data = i.rstrip('\n').split(',')

    if data[3] > '50':
        print(data[1:5])
