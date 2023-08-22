# key : name
# value : weight

dic = {'car': 2000, 'Bike': 700, 'SUV': 5000, 'Bicycle': 200, 'Pickup': 2400, 'Mini': 3000}

# vehicle weight above 2000 names  ===> print in upper case

lst = [i.upper() for i in dic if dic[i] >= 2000]
print(lst)
