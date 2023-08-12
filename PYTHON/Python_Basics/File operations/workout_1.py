# form movies cleaned file
# 1. release year above 2000 name, year, rating, duration
# 2. rating above 3.5 name, year, rating, duration
# 3. year above 2005 and rating above 4, name. year, rating, duration
# 4. Each year released movies count

movies = open('/home/amal/Downloads/movies_cleaned_pandas.csv', 'r')

for i in movies:
    data = i.rstrip('\n').split(',')
    # print(data)
    # years = data[-3]
    # print(data)
    print(data[2])
    year = int(data[2])
    if year >= 2000:
        print(data[1:4])

# code for find movie count after 2000 released
# filtered_dictionary = {}
# year_list_after_2000 = []

#     int_year = int(years)
#     # print(type(int_year))
#     year_list_after_2000.append(int_year)
# # print(year_list_after_2000)
# # print(len(year_list_after_2000))
# for year in year_list_after_2000:
#     # print(year)
#     # print(type(year))
#
#     if year >= 2000:
#         if year not in filtered_dictionary:
#             filtered_dictionary[year] = 1
#         else:
#             filtered_dictionary[year] += 1
#
# for k, v in filtered_dictionary.items():
#     print(k, ",", v)
