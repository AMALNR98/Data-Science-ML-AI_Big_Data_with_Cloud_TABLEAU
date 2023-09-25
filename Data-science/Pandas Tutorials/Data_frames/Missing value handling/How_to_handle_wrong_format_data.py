# handling wrong format data
# example a human height 400cm

import numpy as np
import pandas as pd

movies = pd.read_csv(
    '/home/amal/Downloads/movies.csv')
movies.columns = ['id', 'name', 'year', 'rating', 'duration']
print(movies)
print(movies.shape)

movies.loc[7,'Duration'] = 45       # in 7the row duration changed to 45
print(movies)