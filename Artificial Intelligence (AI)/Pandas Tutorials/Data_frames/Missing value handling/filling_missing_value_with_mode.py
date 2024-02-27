# mode
import pandas as pd

missing_data1 = pd.read_csv(
    '/home/amal/Downloads/missing_data1.csv')
print(missing_data1)
print(missing_data1.shape)

mode_of_calories = missing_data1['Calories'].mode()     # find median of column  or use .mode() [0]
print(mode_of_calories)
missing_data1['Calories'].fillna(mode_of_calories, inplace=True)     # filling in specific column
print(missing_data1)