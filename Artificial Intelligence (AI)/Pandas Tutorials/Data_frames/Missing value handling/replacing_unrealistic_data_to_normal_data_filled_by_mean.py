# 7th Duration 450 ===> 45
# calories ===> 4000 ===> mean()

import numpy as np
import pandas as pd

missing_1 = pd.read_csv('/home/amal/Downloads/missing_data1.csv')
print(missing_1)
print("*" * 100)

calories_mean = missing_1['Calories'].mean()
print(calories_mean)
print("*" * 100)

for x in missing_1.index:
    if missing_1.loc[x, 'Calories'] > 400:
        missing_1.loc[x, 'Calories'] = calories_mean

print(missing_1)
