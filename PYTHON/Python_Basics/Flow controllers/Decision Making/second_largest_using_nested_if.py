"""
Find second-largest number using nested if
num1,num2,num3
num1>num2 and num1>num3
"""

number_1 = int(input("Enter the first number :"))  # 100
number_2 = int(input("Enter the second number :"))  # 80
number_3 = int(input("Enter the third number :"))  # 60

if number_1 > number_2 and number_1 > number_3:  # 100>80 & 100>60
    if number_2 > number_3:  # 80>60
        print(f"{number_2} is the second largest number")
    else:
        print(f"{number_3} is the second largest number")
elif number_2 > number_1 and number_2 > number_3:  # 100>80 & 100>60
    if number_1 > number_3:  # 80>60
        print(f"{number_1} is second largest number")
elif number_3 > number_1 and number_3 > number_2:
    if number_1 > number_2:
        print(f"{number_1} is second largest number")
    else:
        print(f"{number_2} is second largest number")
else:
    print("numbers are equal")
