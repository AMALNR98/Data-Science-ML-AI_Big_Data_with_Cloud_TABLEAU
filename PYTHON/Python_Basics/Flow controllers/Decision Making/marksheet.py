"""
sub1,sub2 ,sub3 ,sub4
    >180 --> A+
    160-179 --> B+
    140-159 --> B
    120-139 --> C+
    100-119 --> C
    Below 80 --> Fail
"""

subject_1 = int(input("Enter the marks for subject 1 : "))
subject_2 = int(input("Enter the marks for subject 2 : "))
subject_3 = int(input("Enter the marks for subject 3 : "))
subject_4 = int(input("Enter the marks for subject 4 : "))

total = subject_1 + subject_2 + subject_3 + subject_4

if total > 180:
    print(f"Your make is {total}, so your grade is A+")
elif 160 > total > 179:
    print(f"Your make is {total}, so your grade is B+")
elif 140 > total > 159:
    print(f"Your make is {total}, so your grade is B")
elif 120 > total > 139:
    print(f"Your make is {total}, so your grade is C+")
elif 100 > total > 119:
    print(f"Your make is {total}, so your grade is C")
else:
    print(f"Your mark is {total}, sorry You are failed")
