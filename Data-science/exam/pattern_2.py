def print_pattern(number):
    for i in range(1, number + 1):
        for j in range(1, number + 1):
            if j <= i:
                print(i, end=" ")
            else:
                print(j, end=" ")
        print()


n = 5
print_pattern(n)
