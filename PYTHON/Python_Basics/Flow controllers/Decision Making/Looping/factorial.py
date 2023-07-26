# To find a factorial of number
# 5! = 5*4*3*2*1

number = int(input("Enter the number"))
fact = 1
i = 1
while i <= number:
    fact = number * i
    i += 1
print(f"The factorial of {number} is : {fact}")
