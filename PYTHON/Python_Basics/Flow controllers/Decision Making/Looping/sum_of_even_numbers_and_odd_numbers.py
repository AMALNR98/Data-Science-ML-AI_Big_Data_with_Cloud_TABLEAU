lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))
lower = lower_limit
upper = upper_limit
sum_of_odd = 0
sum_of_even = 0
while upper >= lower:
    if lower % 2 == 0:
        sum_of_even = sum_of_even + lower
    else:
        sum_of_odd = sum_of_odd + lower
    lower += 1
print(f"Sum of even number is : {sum_of_even}")
print(f"Sum of odd number is : {sum_of_odd}")