# def palindrome(string_for_check):
#     return string_for_check == string_for_check[::-1]
#
#
# string_1 = input("Enter the string")
# check_result = palindrome(string_1)
#
# if check_result:
#     print(f"The given string is palindrome, the string is '{string_1}'")
# else:
#     print(f"The give string is not palindrome, the string is '{string_1}'")
#

n = 7
c = 0
while (n):
    if n > 5:
        c = c + n - 1
        n = n - 1
    else:
        break
print(n)
