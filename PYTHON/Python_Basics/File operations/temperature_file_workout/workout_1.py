# find the highest temperature in each district

"""
district = data[0]
temp= data[1]

"""

temperature = open('/home/amal/Downloads/temper', 'r')
for i in temperature:
    data = i.rstrip('\n').split(',')
