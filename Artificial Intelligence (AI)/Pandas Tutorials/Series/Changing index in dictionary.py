import numpy as np
import pandas as pd

a = pd.Series({'id': 101, 'f_name': 'amal', 'l_name': 'n r', 'age': 30, 'prof': 'big data'},
              index=['first_name', 'last_name', 'age', 'id'])
print(a)
b = pd.Series(a)
print(b)


