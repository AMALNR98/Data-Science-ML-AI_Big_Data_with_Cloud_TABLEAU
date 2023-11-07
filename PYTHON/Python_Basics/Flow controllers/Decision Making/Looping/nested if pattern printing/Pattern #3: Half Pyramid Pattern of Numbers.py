# 1
#
# 1 2
#
# 1 2 3
#
# 1 2 3 4
#
# 1 2 3 4 5

rows = 5
for row in range(1, rows + 1):
    for column in range(1, row+1):
        print(column, end=' ')
    print(' ')

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5