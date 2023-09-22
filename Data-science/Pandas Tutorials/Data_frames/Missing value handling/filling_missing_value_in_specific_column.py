import pandas as pd

missing_data1 = pd.read_csv(
    '/home/amal/Downloads/missing_data1.csv')
print(missing_data1)
print(missing_data1.shape)

missing_data1['Calories'].fillna(200, inplace=True)     # filling in specific column
print(missing_data1)

missing_data1['Date'].fillna("'2020/12/02'",inplace=True)
print(missing_data1)