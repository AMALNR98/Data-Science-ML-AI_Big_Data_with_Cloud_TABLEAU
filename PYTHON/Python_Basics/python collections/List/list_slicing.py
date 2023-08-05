lst = [10, 15, 20, 25, 30, 40, 50, 29, 21, 6, 9, 11, 13, 200]

print(lst[2:6:2])  # index = 2,4 [20,30]
# list[start:stop:step]
# -----------------------
print(lst[4:12:3])  # index = 4, 7, 19  [30,29,9]

print(lst[4::3])  # index = 3,           [30, 29, 9, 200]

print(lst[:9:2])  # index =             [10, 20, 30, 50, 21]

print(lst[:])

print(lst[::5])  # only step

# Positive indexing 0 to n-1   [left to right]
# Negative indexing ==> right to left -1 to -n
