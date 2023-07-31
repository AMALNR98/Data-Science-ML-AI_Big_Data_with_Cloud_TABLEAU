def factorial(number):
    fact = 1
    i = 1
    while i <= number:
        fact = number * i
        i += 1
    return fact

number = int(input("Enter the number : "))
result = factorial(number)
print(f"The result is {result}")