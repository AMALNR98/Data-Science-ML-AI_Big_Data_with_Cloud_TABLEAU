"""
Assignment 1

customer
.................................
1. Find Row count
2. Remove duplicates rows and find total row count
3. Age maximum 10 fname,lname,prof,loc
4. Age minimum 5 employees fname,lname,prof,loc
5. Each location count [count desc order]
6. Full data
7. Each age group count [age desc order]
8. Each profession count [count desc order]
9. India work
A. Row count
B. Each profession count [count desc order]
C. Age mxm 3 employees fname,lname,age,prof
D. Age minimum 3 employees fname,lname,age,prof
E. age above 40 full data
F. age range 30 to 40 [profession count]
10. us work
A. Row count
B. Each age group count
C. Each profession count [count desc]
D. Civil engineer dept and age above 30
"""

import numpy as np
import pandas as pd

customer1 = pd.read_csv('/home/amal/Downloads/customer1.txt', header=None)
customer1.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'location']
customer = customer1.fillna('India')
print(customer)
print("*" * 100)
print(customer1)
print("*" * 100)

print('1. Find Row count')
question_1 = customer.shape[0]
print(question_1)
print("*" * 100)

print("2. Remove duplicates rows and find total row count")
question_2 = customer.drop_duplicates() \
    .shape[0]
print(question_2)
print("*" * 100)

print("3. Age maximum 10 fname,lname,prof,loc")
question_3 = customer1.sort_values(by='age', ascending=False)[['first_name', 'last_name', 'profession']].head(10)
print(question_3)
print("*" * 100)

print('4. Age minimum 5 employees fname,lname,prof,loc')
question_4 = customer1.sort_values(by='age')[['first_name', 'last_name', 'profession', 'location']].head(10)
print(question_4)
print("*" * 100)

print('5. Each location count [count desc order]')
question_5 = customer1.groupby('location')['location'].count().sort_values(ascending=False)
print(question_5)
print("*" * 100)

print("*" * 100)
print('7. Each age group count [age desc order]')
question_7 = customer1.groupby('age')['age'].count().sort_values(ascending=False)
print(question_7)
print("*" * 100)

print('8. Each profession count [count desc order]')
question_8 = customer1.groupby('profession')['profession'].count().sort_values(ascending=False)
print(question_8)
print("*" * 100)

print('9. India work')
indian_customers = customer1.loc[customer1['location'] == 'india']
print(indian_customers)
print("*" * 100)

print('A. Row count')
question_9_a = indian_customers.shape[0]
print(question_9_a)
print("*" * 100)

print('B. Each profession count [count desc order]')
question_9_b = indian_customers.groupby('profession')['profession'].count().sort_values(ascending=False)
print(question_9_b)
print("*" * 100)

print('C. Age mxm 3 employees fname,lname,age,prof')
question_9_c = indian_customers.sort_values(by='age', ascending=False)[['first_name', 'last_name', 'profession']].head(3)
print(question_9_c)
print("*" * 100)

print('D. Age minimum 3 employees fname,lname,age,prof')
question_9_d = indian_customers.sort_values(by='age')[['first_name', 'last_name', 'profession']].head(3)
print("*" * 100)

print('E. age above 40 full data')
question_9_e = indian_customers.loc[indian_customers['age'] >= 40]
print(question_9_e)
print("*" * 100)

print('F. age range 30 to 40 [profession count]')
age_range = indian_customers.loc[(indian_customers['age'] >= 30) & (indian_customers['age'] <= 40)]
# print(age_range)
question_9_f = age_range.groupby('profession')['profession'].count()
print("*" * 100)

print('10. us work')
us_work = customer1.loc[customer1['location'] == 'us']
print(us_work)
print("*" * 100)

print('A. Row count')
question_10_a = us_work .shape[0]
print(us_work)
print("*" * 100)

print('B. Each age group count')
question_10_b = us_work.groupby('age')['age'].count()
print(question_10_b)
print("*" * 100)

print('C. Each profession count [count desc]')
question_10_c = us_work.groupby('profession')['profession'].count().sort_values(ascending=False)
print(question_10_c)
print("*" * 100)

print('D. Civil engineer dept and age above 30')
question_10_d = us_work.loc[(us_work['age'] >= 30) & (us_work['profession'] == 'Civil engineer')]
print(question_10_d)
print("*" * 100)
