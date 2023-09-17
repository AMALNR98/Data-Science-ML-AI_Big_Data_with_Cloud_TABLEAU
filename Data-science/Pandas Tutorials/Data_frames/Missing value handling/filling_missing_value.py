import numpy as np
import pandas as pd

customer1 = pd.read_csv(
    '/home/amal/Downloads/customer1.txt', header=None)
customer1.columns = ['id', 'first_name', 'last_name', 'age', 'prof', 'location']
print(customer1)

# filling missing value

# fillna()

print(("*" * 100))
customer1_with_filling = customer1.fillna('India')
print(customer1_with_filling)

print("*" * 100)
print(customer1_with_filling.isna().sum())
