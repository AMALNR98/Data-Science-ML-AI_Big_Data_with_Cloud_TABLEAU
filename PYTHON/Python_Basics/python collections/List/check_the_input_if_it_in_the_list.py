lst_1 = [4, 1, 0, 9, 15, 13, 50, 31, 29, 44]
value = int(input('Enter the value : '))
for i in lst_1:
    if value == i:
        print(f"The value {value} is present in the list")
        break

print("The value is not found")