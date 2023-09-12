import numpy as np
import pandas as pd

a = pd.Series({'id': 101, 'fname': 'amal', 'lname': 'n r', 'age': 30})
print(a)
b = pd.Series(a)
print(b)

# here key is index
