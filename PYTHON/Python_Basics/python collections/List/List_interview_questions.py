# question 1
from speechd_config import question

lst = [3, 5, 10, 20, 25, 30, 15]
# predict  result
print(lst[-0] + lst[-1] + lst[2])
# ans:
#       28
print(lst[-0])
print(lst[-1])
print(lst[2])

# question 2
lst_1 = [4, 10, 6, 20, 15, 25, 12, 8]
# Form this list create
# lst_2 = [96, 90, 6, 20, 15, 25, 12, 8]

# ans:
empty_lst = []
result = add(lst_1)
for i in lst_1:
    empty_lst.append(result - i)
print(empty_lst)

# question 3
lst_2 = [1, 5, 6, 3, 2, 4, 5, 2, 1, 6, 7, 8, 9, 3, 1, 7, 8, 9, 11, 9, 6, 5, 4, 3]

# create list form this
# [1,6,2,5,1,9,1,11]
# when ever the series is increase and decrease


# ?????????????????????????????????????????????????????????????????????


# question 4:
lst_4 = [1, 4, 6, 7, 9, 11, 15, 20, 25, 40, 50]
print(15 not in lst_4)  # if 15 not in lst_4 it will print "False"
print(1 in lst_4)  # if 1 is in lst_4 it will print "True"

# question 5:
string = 'luminartechnolab'
vowels = 'aeiouAEIOU'
for i in string:
    if i in vowels:
        print(i)

# question 6: find count of vowels


add = 0
for i in string:
    if i in vowels:
        add += 1

print(add)

# count number of non-vowels
sum_of = []
for i in string:
    if i not in vowels:
        sum_of.append(i)
print(len(sum_of))
