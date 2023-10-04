def prime(lower_value, upper_value):
    list_of_prime_number = []
    flag = 0
    for i in range(lower_value, upper_value):
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            list_of_prime_number.append(i)
    return list_of_prime_number


lower = 0
upper = 100
list_of_prime = prime(lower, upper)
print(f"The prime numbers are : {list_of_prime}")
