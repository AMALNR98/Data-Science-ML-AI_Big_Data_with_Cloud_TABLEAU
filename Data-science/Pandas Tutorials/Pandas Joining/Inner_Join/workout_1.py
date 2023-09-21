import numpy as np
import pandas as pd

custom = pd.read_csv('/home/amal/Downloads/custom.txt', header=None)
custom.columns = ['id', 'name', 'age', 'loc', 'salary']
print(custom)
print("*" * 100)
order = pd.read_csv('/home/amal/Downloads/order.txt', header=None)
order.columns = ['id', 'date', 'quantity', 'amount']
print(order)

# name, age, date, amount
# salary above 2000 name, age, salary, date, amount
# salary above 2000 and amount above 15000 name, age, location, date amount
# age mxm 1 employee name, age, salary, date, amount
# latest_date purchase 1 name, age, salary, date, amount

question_1 = pd.merge(custom, order, on='id', how='inner')[['name', 'age', 'date', 'amount']]
print(question_1)

question_2 = pd.merge(custom, order, on='id', how='inner').loc[custom['salary'] > 2000][
    ['name', 'age', 'salary', 'date', 'amount']]
print(question_2)

question_3 = pd.merge(custom, order, on='id', how='inner').loc[(custom['salary'] > 2000) & (order['amount'] > 1500)] \
    [["name", 'age', 'date', 'amount']]
print(question_3)

question_4 = pd.merge(custom, order, on='id', how='inner') \
    .sort_values(by='age', ascending=False) \
    [['name', 'age', 'salary']].head(1)
print(question_4)

question_5 = pd.merge(custom, order, on='id', how='inner') \
    .sort_values(by='age') \
    [['name', 'age', 'salary']].head(1)
print(question_5)
