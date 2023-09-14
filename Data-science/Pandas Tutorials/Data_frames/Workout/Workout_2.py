# customer1.txt ===> first_name, last_name, age,prof
import numpy as np
import pandas as pd

customer1 = pd.read_csv(
    '/home/amal/Downloads/customer1.txt', header=None)
customer1.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'country']
print(customer1)
