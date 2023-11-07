# 5 5 5 5 5
#
# 5 5 5 5
#
# 5 5 5
#
# 5 5
#
# 5

rows = 5
num = rows
for row in range(rows, 0, -1):
    for j in range(0, row):
        print(rows, end=' ')
    print("\r")

# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5