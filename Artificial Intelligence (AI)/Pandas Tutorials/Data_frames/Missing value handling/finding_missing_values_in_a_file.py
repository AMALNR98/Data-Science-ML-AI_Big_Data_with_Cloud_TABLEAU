import numpy as np
import pandas as pd

customer1 = pd.read_csv(
    '/home/amal/Downloads/customer1.txt', header=None)
customer1.columns = ['id', 'first_name', 'last_name', 'age', 'prof', 'location']
print(customer1)
print("*" * 100)
# isna().sum() ----> used  to find number of missing values

print(customer1.isna().sum())
