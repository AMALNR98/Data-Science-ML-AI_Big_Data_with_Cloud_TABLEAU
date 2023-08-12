# 3. year above 2005 and rating above 4, name. year, rating, duration

movies = open('/home/amal/Downloads/movies_cleaned_pandas.csv', 'r')

for i in movies:
    data = i.rstrip('\n').split(',')
    rating = float(data[3])
    year = int(data[2])
    if rating >= 4 and year >= 2005:
        print(data[1:5])
