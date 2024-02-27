# id, first_name, last_name, age, profession, location

# x(customer1_except_last_column)= id, first_name, last_name, age, profession
# y= only need last column

import numpy as np
import pandas as pd

customer1 = pd.read_csv(
    '/home/amal/Downloads/customer1.txt', header=None)
customer1.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'country']

customer1_except_last_column = customer1.iloc[:, :-1]
print(customer1_except_last_column)

y = customer1.iloc[:, -1]
print(y)
