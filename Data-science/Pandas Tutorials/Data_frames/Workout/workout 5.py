"""
customer1.txt
1. Age mxm 5 customer first_name, last_name, age, profession
2. Age minimum 3 customer first_name, last_name, age, profession
3. india work data
4. India and age above 50 first_name, last_name, age, profession
5. UK and age less than 30 first_name, last_name, age, profession
6. Doctor profession work
7. India work and profession first_name, last_name, age
8. India, profession - Doctor, age mxm 1 employee first_name, last_name, age
9. Pilot profession age mxm 1 employee first_name, last_Name, age, location
10. Pilot profession age minimum 1 employee full data
11. Age range 25 to 40 first_name, last_name, age, profession, location
"""

import numpy as np
import pandas as pd

customer1 = pd.read_csv('/home/amal/Downloads/customer1.txt', header=None)
customer1.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'location']
print("*" * 100)
print(customer1)

print("*" * 100)
print("1. Age mxm 5 customer first_name, last_name, age, profession")
print("*" * 75)
question_1 = customer1.sort_values(by='age')[['first_name', 'last_name', 'age', 'profession']].head(5)
print(question_1)
print("*" * 100)

print("2. Age minimum 3 customer first_name, last_name, age, profession")
print("*" * 75)
question_2 = customer1.sort_values(by='age', ascending=False)[['first_name', 'last_name', 'age', 'profession']].head(3)
print(question_2)
print("*" * 100)

print("3. india work data")
print("*" * 75)
question_3 = customer1.loc[customer1['location'] == 'india'][['first_name', 'last_name', 'age', 'location']]
print(question_3)
print("*" * 100)

print("4. India and age above 50 first_name, last_name, age, profession")
print("*" * 75)
question_4 = customer1.loc[customer1['location'] == 'india'] \
    .sort_values(by='age', ascending=False) \
    [['first_name', 'last_name', 'age', 'profession']]
print(question_4)
print("*" * 100)

print("5. UK and age less than 30 first_name, last_name, age, profession")
print("*" * 75)
question_5 = customer1.loc[(customer1['location'] == 'uk') & (customer1['age'] < 30)] \
    [['first_name', 'last_name', 'age', 'profession']]
print(question_5)
print("*" * 100)

print("6. Doctor profession work")
print("*" * 75)
question_6 = customer1.loc[(customer1['location'] == "india")]
print(question_6)
print("*" * 100)

print("7. India work and profession doctor first_name, last_name, age")
print("*" * 75)
question_7 = customer1.loc[(customer1['location'] == 'india') & (customer1['profession'] == 'Doctor')]
print(question_7)
print("*" * 100)

print("8. India, profession - Doctor, age mxm 1 employee first_name, last_name, age")
print("*" * 75)
question_8 = customer1.loc[(customer1['location'] == 'india') & (customer1["profession"] == "Doctor")] \
    .sort_values(by='age', ascending=False)[['first_name', 'last_name', 'age']]
print(question_8)
print("*" * 100)

print("9. Pilot profession age mxm 1 employee first_name, last_Name, age, location")
print("*" * 75)
question_9 = customer1.loc[(customer1['profession'] == 'Pilot')] \
    .sort_values(by='age', ascending=False) \
    [['first_name', 'last_name', 'age', 'profession', 'location']].head(1)
print(question_9)
print("*" * 100)

print("10. Pilot profession age minimum 1 employee full data")
print("*" * 75)
question_10 = customer1.loc[(customer1['profession'] == "Pilot")] \
    .sort_values(by='age', ascending=False)
print(question_10)
print("*" * 100)

print("11. Age range 25 to 40 first_name, last_name, age, profession, location")
print("*" * 75)
question_11 = customer1.loc[(customer1['age'] < 40) & (customer1['age'] > 25)]\
                        [['first_name', 'last_name', 'age', 'profession', 'location']]
print(question_11)
print("*" * 100)
