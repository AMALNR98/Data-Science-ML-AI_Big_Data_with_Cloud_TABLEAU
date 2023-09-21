"""
1. Find row count
2. Remove duplicates and find row count
3. Sort data set by release year in des order
4. Find rating mxm 5 movies name,year,rating
5. Find rating minimum 3 movies name,year,rtaing
6. Find Each year release movie count [count desc order]
7. Each rating count [count desc order]
8. 2008 and rating above 3 [collect]
    A. row count
9. Find duration mxm 1 movies name,year,rating,duration
10. Find rating mnm 1 movies name,year,rating,duration
11. Rating above 4 and release year above 2005
    A. Rating mxm movies full data
    B. Rating mnm movies full data
12. 2008 movies count
13. 1975-2000 movies collect
    A. Row count
14. 1975-2000 and rating above 3.5 total row count
"""
import numpy as np
import pandas as pd

movies = pd.read_csv('/home/amal/Downloads/movies_cleaned_pandas.csv', header=None)
movies.columns = ['id', 'movie', 'year', 'rating', 'duration']
print(movies)
print("*" * 150)

print('1. Find row count')
question_1 = movies.shape[0]
print(question_1)
print("*" * 150)

print('2. Remove duplicates and find row count')
question_2 = movies.drop_duplicates()
print(question_2)
print("*" * 150)

print('3. Sort data set by release year in des order')
question_3 = movies.sort_values(by='rating', ascending=False)
print(question_3)
print("*" * 150)

print('4. Find rating mxm 5 movies name,year,rating')
question_4 = movies.sort_values(by='rating', ascending=False)[['movie', 'year', 'rating']].head(5)
print(question_4)
print("*" * 150)

print('5. Find rating minimum 3 movies name,year,rtaing')
question_5 = movies.sort_values(by='rating')[['movie', 'year', 'rating']].head(3)
print(question_5)
print("*" * 150)

print('6. Find Each year release movie count [count desc order]')
question_6 = movies.groupby('year') ['year'].count()
print(question_6)
print("*" * 150)

print('7. Each rating count [count desc order]')
question_7 = movies.groupby('rating') ['rating'].count()
print(question_7)
print("*" * 150)

print('8. 2008 and rating above 3 [collect]')
question_8 = movies.loc[(movies['year'] >= 2008) & (movies['rating'] > 3)]
print(question_8)
print('    A. row count')
question_8_b =question_8.shape[0]
print("*" * 150)

print('9. Find duration mxm 1 movies name,year,rating,duration')
question_9 = movies.sort_values(by='rating', ascending=False)[['movie', 'year', 'rating']].head(1)
print(question_9)
print("*" * 150)

print('10. Find rating mnm 1 movies name,year,rating,duration')
question_10 = movies.sort_values(by='rating')[['movie', 'year', 'rating']].head(1)
print(question_10)
print("*" * 150)

print('11. Rating above 4 and release year above 2005')
question_11 = movies.loc[(movies['year'] > 2005) & (movies['rating'] > 4)]
print(question_11)
print("*" * 150)

print('    A. Rating mxm movies full data')
question_11_a = question_11.sort_values(by='rating').head(1)
print(question_11_a)
print("*" * 150)

print('    B. Rating mnm movies full data')
question_11_b = question_11.sort_values(by='rating', ascending=False).head(1)
print(question_11_b)
print("*" * 150)

print('12. 2008 movies count')
question_12 = movies.loc[(movies['year'] == 2008)]
# question_12.columns = ['year','count']
# print(question_12)
year_2008 = question_12.shape[0]
print(year_2008)
print("*" * 150)

print('13. 1975-2000 movies collect')
question_13 = movies.loc[(movies['year'] > 1975) & (movies['year'] < 2000)]
print(question_13)
print("*" * 150)
print('    A. Row count')
question_13_a = question_13.shape[0]
print(question_13_a)
print("*" * 150)

print('14. 1975-2000 and rating above 3.5 total row count')
question_14 = movies.loc[(movies['year'] > 2000) & (movies['rating'] > 3.5)]
question_14_count = question_14.shape[0]
print(question_14_count)
