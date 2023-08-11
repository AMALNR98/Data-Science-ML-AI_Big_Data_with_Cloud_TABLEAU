customer = open('/home/amal/Downloads/customer1.txt', 'r')


for i in customer:
    data = i.rstrip('\n').split(',')
    age = data[3]
    loc = data[-1]
    if loc == 'india' and age > '50':
        print(data[1:5])
