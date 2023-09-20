import numpy as np
import pandas as pd

customer1 = pd.read_csv('/home/amal/Downloads/customer1.txt', header=None)
customer1.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'location']
print("*" * 100)
print(customer1)

customer1_count = customer1.groupby('profession') ['profession'].count().sort_values(ascending=False)
print(customer1_count)

# india each profession
customer1_india_prof = customer1.loc[customer1['location']=='india']\
                                .groupby('profession') ['profession'].count()\
                                .sort_values(ascending=False)
print(customer1_india_prof)