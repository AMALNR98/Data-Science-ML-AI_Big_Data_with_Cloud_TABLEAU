# sample_4.txt,
# customer,
# customer5.txt to dataframe

import numpy as np
import pandas as pd

sample_4 = pd.read_csv(
    '/home/amal/Downloads/sample4.txt',header=None)  # if the file is comma separation there is no need to define
print(sample_4)
print("*" * 100)

customer = pd.read_csv(
    '/home/amal/Downloads/customer1.txt',header=None)

customer_5 = pd.read_csv(
    '/home/amal/Downloads/customer5.txt',header=None)
print(customer_5)
print("*" * 100)

# customer_5.columns = ['id', 'name', 'age', 'place', 'salary']
print(customer_5)