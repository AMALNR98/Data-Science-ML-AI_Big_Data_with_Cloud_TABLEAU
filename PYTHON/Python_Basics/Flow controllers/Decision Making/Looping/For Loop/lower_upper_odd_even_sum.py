number = int(input("Enter the number : "))
even_sum = 0
odd_sum = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"The even sum is {even_sum}")
print(f"The odd sum is {odd_sum}")
