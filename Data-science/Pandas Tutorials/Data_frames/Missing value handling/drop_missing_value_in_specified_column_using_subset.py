import pandas as pd

missing_data1 = pd.read_csv(
    '/home/amal/Downloads/missing_data1.csv')
print(missing_data1)
print(missing_data1.shape)

missing_data1.dropna(subset=['Calories'],inplace=True)
print(missing_data1)