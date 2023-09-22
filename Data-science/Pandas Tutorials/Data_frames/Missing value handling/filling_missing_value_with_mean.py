# mean : average value
import pandas as pd

missing_data1 = pd.read_csv(
    '/home/amal/Downloads/missing_data1.csv')
print(missing_data1)
print(missing_data1.shape)

mean_of_calories = missing_data1['Calories'].mean()     # find mean of column
print(mean_of_calories)
missing_data1['Calories'].fillna(mean_of_calories, inplace=True)     # filling in specific column
print(missing_data1)