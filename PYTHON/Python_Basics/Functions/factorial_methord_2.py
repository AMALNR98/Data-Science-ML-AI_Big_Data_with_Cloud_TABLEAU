def factorial(number):
    fact = 1
    i = 1
    while i <= number:
        fact = number * i
        i += 1
    print(f"The factorial of {number} is : {fact}")


factorial(5)
