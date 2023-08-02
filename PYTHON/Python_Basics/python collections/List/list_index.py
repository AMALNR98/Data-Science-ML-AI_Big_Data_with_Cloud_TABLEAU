lst = [10, 20, 35, 67, 45, 50, 68, 43]
print(lst)  # index 0....to....n-1
print(lst[1])
print(lst[5])
print(lst[7])

# To assign value to a location
lst[1] = 100
print(lst)  # here 20 replaced by 100

# 50 ====> 'python'
# 43 ====> 72.5
# 67 ====> 120

lst[5] = 'python'
print(lst)

lst[7] = 72.5
print(lst)

lst[3] = 120
print(lst)

for i in lst:
    print(i)


