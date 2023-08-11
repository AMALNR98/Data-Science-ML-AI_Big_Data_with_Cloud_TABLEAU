customer = open('/home/amal/Downloads/customer1.txt', 'r')


for i in customer:
    data = i.rstrip('\n').split(',')
    if data[-1] == 'india':  # here a missing value occurred so use negative indexing
        print(data[1:5])
