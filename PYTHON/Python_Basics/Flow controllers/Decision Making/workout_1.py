#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years
#Ask user for their salary and year of service and print the net bonus amount

service = int(input("Enter the service"))

if(service >= 5):
    salary = int(input("Enter the salary"))
    bonus = salary * (5/100)
    print(f"The bonus amount is {bonus}")
else:
    print("not eligible for bonus")