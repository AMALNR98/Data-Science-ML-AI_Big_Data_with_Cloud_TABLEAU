# 4. Each year released movies count


movies = open('/home/amal/Downloads/movies_cleaned_pandas.csv', 'r')
filtered_dictionary = {}
year_list_after_2000 = []

for i in movies:
    data = i.rstrip('\n').split(',')
    years = data[-3]
    int_year = int(years)
    # print(type(int_year))
    year_list_after_2000.append(int_year)
    # print(year_list_after_2000)
    # print(len(year_list_after_2000))
for year in year_list_after_2000:
    # print(year)
    # print(type(year))

    if year >= 2000:
        if year not in filtered_dictionary:
            filtered_dictionary[year] = 1

        else:
            filtered_dictionary[year] += 1

for k, v in filtered_dictionary.items():
    print(k, ",", v)
