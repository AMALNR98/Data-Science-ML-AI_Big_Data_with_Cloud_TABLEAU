# Nested list : list passes inside a list

employee_list = [[101, 'vinay', 'p', 28, 'bigdata', 1000],
                 [102, 'anu', 'r', 29, 'python', 2000],
                 [103, 'amal', 'p', 26, 'bigdata', 25000],
                 [104, 'arjun', 'k', 31, 'pyton', 3000],
                 [105, 'mani', 'a', 32, 'bigdata', 1750],
                 [106, 'kamal', 'n', 34, 'bigdata', 1850],
                 [107, 'sabir', 'j', 37, 'bigdata', 1550],
                 [108, 'vishnu', 'n', 31, 'bigdata', 1250],
                 ]
# print(employee_list)
# for i in employee_list:
#     print(i)

# age above 28 fname,lname,age

# for i in employee_list:
#     if i[3] > 28:
#         print(i[1], i[2], i[3])
#         # print(i[1:4])

# bigdata prof fname,lname,age,prof
# for i in employee_list:
#     if i[4]== 'bigdata':
#         print(i[1:5])

# python prof fname,age,salary
# for i in employee_list:
#     if i[4] == 'python':
#         print(i[1], i[3], i[5])

# worked in bigdata and age above 28 fname, lanme, age

# for i in employee_list:
#     if i[4] == 'bigdata' and i[3] < 28:
#         print(i[1], i[2], i[5])

# Total salar
sum_ = 0
for i in employee_list:
    sum_ += i[5]
    #sum_ += i[-1]
print(sum_)


# sum, max,min is not applicable in nested list