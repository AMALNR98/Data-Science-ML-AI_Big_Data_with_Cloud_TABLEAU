# ioc

import numpy as np
import pandas as pd

customer1 = pd.read_csv(
    '/home/amal/Downloads/customer1.txt', header=None)
customer1.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'country']
print(customer1)

customer1_wanted_row = customer1.iloc[3:7]
print(customer1_wanted_row)

customer1_wanted_row_1 = customer1.iloc[3:, 1:4]  # collecting rows and columns
print(customer1_wanted_row_1)
