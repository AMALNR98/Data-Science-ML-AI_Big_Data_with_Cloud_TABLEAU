# 5 5 5 5 5
#
# 4 4 4 4
#
# 3 3 3
#
# 2 2
#
# 1

rows = 5
for row in range(rows, 0, -1):
    for i in range(0, row):
        print(row, end=" ")
    print('\r')

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1