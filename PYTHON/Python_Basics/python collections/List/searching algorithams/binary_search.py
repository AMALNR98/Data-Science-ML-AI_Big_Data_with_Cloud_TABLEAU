# Binary search algorithm
from typing import List

# steps :
# 1. Sort the given list in ascending order
# 2. Set 2 variables "lower = 0" and "upper = len(list) - 1
# 3. Calculate : "mid =(low + upper) // 2"
# 4. set 2 conditions
#   A. if search > list[mid]
#           low = mid + 1
#   B. if search < list[mid]
#           upper = mid - 1
#   C. if search == list[mid]
#           element found

lst_1 = [4, 1, 0, 9, 15, 13, 50, 31, 29, 44]
lower = 0
upper = len(lst_1) - 1
flag = 0

lst_1.sort()
element = int(input("Enter the number : "))

while(lower < upper):
    mid = (lower+upper)//2
    if element > lst_1[mid]:
        lower = mid+1
    elif element < lst_1[mid]:
        upper = mid-1
    elif element == lst_1[mid]:
        flag = 1
        break
if flag > 0:
    print("Element found")
else:
    print("Element is not found")