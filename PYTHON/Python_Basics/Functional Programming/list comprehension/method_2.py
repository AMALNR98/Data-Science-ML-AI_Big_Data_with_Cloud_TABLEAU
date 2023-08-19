# Method 2
# [Printing range if condition]

# 1 - 30 range, even
lst = [i for i in range(1, 31) if i % 2 == 0]
print(lst)

# 1 to 50 range, odd number
lst_2 = [i for i in range(1, 51) if i % 2 == 1]
print(lst_2)

# 1 to 50 range, divisible by 5
lst_3 = [i for i in range(1, 51) if i % 5 == 0]
print(lst_3)

# 1 to 30 range even number square
lst_4 = [(i, i ** 2) for i in range(1, 31) if i % 2 == 0]
print(lst_4)

#
#

# count number of vowels using list comprehension
string = 'Luminartechnolab'
vowels = 'aeiouAEIOU'

print("length of string is : ", len(string))
lst_5 = [i for i in string if i in vowels]
print("number of vowels in string : ", len(lst_5))

# count number of non-vowels using list comprehension

lst_6 = [ i for i in string if i not in vowels]
print("number of non-vowels in string : ", len(lst_6))
