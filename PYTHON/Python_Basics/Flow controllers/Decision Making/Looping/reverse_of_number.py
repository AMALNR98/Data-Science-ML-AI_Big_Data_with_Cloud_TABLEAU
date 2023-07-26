# Reverse of a number
number = int(input("Enter the number"))
result = 0

while number != 0:
    digit = number % 10
    result = result * 10 + digit
    number = number // 10

print(f"The reverse value is :{result}")
