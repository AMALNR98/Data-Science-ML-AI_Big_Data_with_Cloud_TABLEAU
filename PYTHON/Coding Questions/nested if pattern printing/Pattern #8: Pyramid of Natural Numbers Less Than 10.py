# 1
#
# 2 3 4
#
# 5 6 7 8 9

rows = 3
current_number = 1
stop = 2
for i in range(rows):
    for columns in range(1, stop):
        print(current_number, end=' ')
        current_number += 1
    print(' ')
    stop += 2

# 1
# 2 3 4
# 5 6 7 8 9 