# clean movis.csv

import numpy as np
import pandas as pd

movies = pd.read_csv(
    '/home/amal/Downloads/movies.csv')
movies.columns = ['id', 'name', 'year', 'rating', 'duration']
print(movies)
print(movies.shape)
print(movies.isna().sum())
print("*" * 100)

mean_of_rating = movies['rating'].mean()
print(mean_of_rating)
movies['rating'].fillna(mean_of_rating, inplace=True)
print(movies)

mean_of_duration = movies['duration'].mean()
print(mean_of_duration)
movies['duration'].fillna(mean_of_duration, inplace = True)
print(movies)