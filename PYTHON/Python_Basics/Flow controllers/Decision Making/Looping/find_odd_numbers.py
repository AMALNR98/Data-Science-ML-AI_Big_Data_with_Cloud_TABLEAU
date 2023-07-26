# read upper and lower limit from console
# print all the odd numbers

lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))

while upper_limit >= lower_limit:
    if lower_limit % 2 != 0:
        print(lower_limit)
    lower_limit += 1
