# Assignment
# 1. Find all of the numbers from 1-1000 that are divisible by 8
# 2. find all of the number from 1-1000 that have 6 in them
# 3. Count number of spaces in a string
# 4. Remove all fo the vowels in string
# 5. Find all of the word in a string that are less than 5 letters
# 6. find number of vowels in string

# "Practice problems to drill list comprehension in your head"

string_1 = "Practice problems to drill list comprehension in your head"
vowels = "aeiouAEIOU"
# 1
lst_1 = [i for i in range (1, 1001) if i % 8 == 0]
print(lst_1)

# 2
lst_2 = [i for i in range (1, 1000) if '6' in str(i)]
print(lst_2)

# 3
lst_3 = [i for i in string_1 if i == " "]
print(len(lst_3))

# 4
lst_4 = [i for i in string_1 if i in vowels]
print(lst_4)

# 5
lst_5 = [i for i in string_1.split(" ") if len(i) < 5]
print(lst_5)

#6
print("Number of vowels is : ",len(lst_4))