#swapping without 3rd variable
num_1 = 10
num_2 = 20

print(f"numbers before swapping is {num_1} and {num_2}")

num_1 = num_1 - num_2   #10 - 20 = -10
num_2 = num_1 + num_2   #-10 + 20 = 10
num_1 = num_2 - num_1   # -10 - -10 = 20

print(f"after swapping is {num_1} and {num_2}")