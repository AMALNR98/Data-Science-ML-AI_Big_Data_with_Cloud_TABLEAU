number = int(input("Enter the number :"))
flag = 0
if number == 1:
    print(f"{number} is not a prime number")
elif number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            flag = 1
            break
if flag != 0:
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")