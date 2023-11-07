# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end="*")
    print("@")

# @
# 1*@
# 2*2*@
# 3*3*3*@
# 4*4*4*4*@
# 5*5*5*5*5*@