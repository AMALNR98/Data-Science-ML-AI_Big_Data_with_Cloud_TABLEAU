''' A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not. '''

number_of_classes_held = int(input("Enter the number classes held: "))
number_of_classes_attended = int(input("Enter the number of classes attended: "))

print(f"The number of classes held is: {number_of_classes_held}")
print(f"The number of classes attended by the student is: {number_of_classes_attended}")

percentage = (number_of_classes_attended/number_of_classes_held)*100

if(percentage >= 75):
    print(f"the percentage is {percentage} so the student can attend the exam")
else:
    print(f"the percentage is {percentage} so the student cannot attended the exam")
