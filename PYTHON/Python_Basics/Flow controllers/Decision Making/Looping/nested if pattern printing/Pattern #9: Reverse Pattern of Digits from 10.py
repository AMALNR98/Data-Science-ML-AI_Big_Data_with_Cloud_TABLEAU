# 1
#
# 3 2
#
# 6 5 4
#
# 10 9 8 7

start = 1
stop = 2
currentNumber = stop
for row in range(2, 6):
    for col in range(start, stop):
        currentNumber -= 1
        print(currentNumber, end=' ')
    print("")
    start = stop
    stop += row
    currentNumber = stop

# 1
# 3 2
# 6 5 4
# 10 9 8 7