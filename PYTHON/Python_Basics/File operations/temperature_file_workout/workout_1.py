# find the highest temperature in each district

"""
district = data[0]
temp= data[1]

"""

temperature = open('/home/amal/Downloads/temper', 'r')
dict1 = {}
for i in temperature:
    data = i.rstrip('\n').split(',')
    district = data[0]
    temp = data[1]
    if district not in dict1:
        dict1[district] = temp
    else:
        old = dict1[district]
        if temp > old:
            dict1[district] = temp
print(dict1)
