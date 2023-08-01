# Create a calculator usein function
"""
 Select Operation
1. Addition
2. Subtraction
3. Multiplication
4. Division

Read your choice :
 num1
 num2
"""


def addition(number_1, number_2):
    result = number_1 + number_2
    return result


def subtraction(number_1, number_2):
    result = number_1 - number_2
    return result


def division(number_1, number_2):
    result = number_1 / number_2
    return result


def multiplication(number_1, number_2):
    result = number_1 * number_2
    return result


print("Enter the choice \n1. Addition \n2. Subtraction\n3. Multiplication\n4. Division")
number_1 = int(input("Enter the first number"))
number_2 = int(input("Enter the second number"))
choice = int(input("Enter the choice"))

if choice == 1:
    sum = addition(number_1, number_2)
    print(f"T{number_1} + {number_2} = {sum}")

elif choice == 2:
    div = subtraction(number_1, number_2)
    print(f"{number_1} - {number_2} = {div}")

elif choice == 3:
    mul = multiplication((number_1, number_2))
    print(f"{number_1} * {number_2} = {mul}")

elif choice == 4:
    print(f"{number_1} - {number_2} = {division(number_1, number_2)}")

else:
    print("Invalid choice")


