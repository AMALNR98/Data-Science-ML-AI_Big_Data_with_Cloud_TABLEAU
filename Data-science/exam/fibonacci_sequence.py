# 2. Python program to print the Fibonacci sequence of a given number

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


number_1 = int(input("Enter the number : "))
for i in range(1, number_1):
    print(fibonacci(i))
