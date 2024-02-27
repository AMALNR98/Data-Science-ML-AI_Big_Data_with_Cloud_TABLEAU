"""
customer5.txt

1. Each prof count == count desc

2. Each prof total salary [salary desc]

3. Each country maximum salary [salary desc]

4. Each country average salary

5. Each profession min salary

6. Each age group total salary
"""
import numpy as np
import pandas as pd

customer = pd.read_csv('/home/amal/Downloads/customer5.txt', header=None)
customer.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'location', 'salary']
print(customer)
print("*" * 150)

question_1 = customer.groupby('profession')['profession'].count().sort_values(ascending=False)
print(question_1)
print("*" * 150)

question_2 = customer.groupby('profession')['salary'].count().sort_values(ascending=False)
print(question_2)
print("*" * 150)

question_3 = customer.groupby('location')['salary'].max().sort_values(ascending=False)
print(question_3)
print("*" * 150)

question_4 = customer.groupby('profession')['salary'].mean()
print(question_4)
print("*" * 150)

question_5 = customer.groupby('profession')['salary'].min()
print(question_5)
print("*" * 150)

question_6 = customer.groupby('age')['salary'].sum()
print(question_6)
print("*" * 150)
