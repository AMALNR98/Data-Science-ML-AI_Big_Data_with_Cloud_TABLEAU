# movies.csv

# rating ===> mean
# duration ==> median

import numpy as np
import pandas as pd

missing_1 = pd.read_csv('/home/amal/Downloads/movies_cleaned_pandas.csv')
missing_1.columns = ['id', 'name', 'year', 'rating', 'duration']

print(missing_1)
print("*" * 100)

print(missing_1.isna().sum())
rating_mean = missing_1['rating'].mean()
duration_median = missing_1['duration'].median()

print("*" * 100)
missing_1['rating'].fillna(rating_mean, inplace=True)
missing_1['duration'].fillna(duration_median, inplace=True)

