# 1
#
# 2 1
#
# 3 2 1
#
# 4 3 2 1
#
# 5 4 3 2 1

rows = 6
for row in range(1, rows):
    for j in range(row, 0, -1):
        print(j, end=" ")
    print('\r')

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
