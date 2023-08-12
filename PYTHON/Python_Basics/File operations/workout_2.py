# 2. rating above 3.5 name, year, rating, duration

movies = open('/home/amal/Downloads/movies_cleaned_pandas.csv', 'r')

for i in movies:
    data = i.rstrip('\n').split(',')
    rating = float(data[3])
    # print(rating)

    if rating >= 3.5:
        print(data[1:5])