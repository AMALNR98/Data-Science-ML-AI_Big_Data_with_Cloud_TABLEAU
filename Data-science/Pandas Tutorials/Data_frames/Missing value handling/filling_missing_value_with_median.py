# median : middle value of values in ascending order
import pandas as pd

missing_data1 = pd.read_csv(
    '/home/amal/Downloads/missing_data1.csv')
print(missing_data1)
print(missing_data1.shape)

median_of_calories = missing_data1['Calories'].median()     # find median of column
print(median_of_calories)
missing_data1['Calories'].fillna(median_of_calories, inplace=True)     # filling in specific column
print(missing_data1)