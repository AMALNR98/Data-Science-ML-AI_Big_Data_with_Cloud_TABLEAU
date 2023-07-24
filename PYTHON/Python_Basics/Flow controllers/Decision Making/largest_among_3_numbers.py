""" Find second-largest number """

number_1 = int(input("Enter the first number :"))  # 80
number_2 = int(input("Enter the second number :"))  # 60
number_3 = int(input("Enter the third number :"))  # 100

if (number_1 >= number_2) and (number_1 >= number_3):  # 80>100 & 80>60 ==> f&t==>f  80>60>100
    largest = number_1
elif (number_2 >= number_1) and (number_2 >= number_3):  # 100>80 & 100>60 ==>t&t ==t  60>80>100
    largest = number_2
else:
    largest = number_3

print(f"The largest number is {largest}")
