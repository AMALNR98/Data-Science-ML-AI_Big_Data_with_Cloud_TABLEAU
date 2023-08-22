# range 1 to 50
# 1-15 ===> small
# 16 - 35 ===> medium
# 36 - 50 ===> large


lst = [(i, 'small') if i <= 15 else  (i,'medium') if 16<=i<=35 else (i,'large')  for i in range(1,51)]
print(lst)