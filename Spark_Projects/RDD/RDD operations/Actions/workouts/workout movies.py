'''
1. Each year release movie count
2. 2000 above name,year,ration
3. rating above 4 name,year,rating,duration
4. Rating min 2 moives name, year, rating,duration
5. year above 2005 and rating above 3.5 name, year, rating, duration

'''
from pyspark import SparkContext

sc = SparkContext(master='local', appName='dec').getOrCreate()
rdd = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/RDD operations/Transformation/files/movies_cleaned_pandas.csv')
rdd.foreach(print)
print('*' * 50)

# 2. 2000 above name,year,ration
rdd_q_2 = rdd.map(lambda x:x.split(',')).filter(lambda x: x[2] >= '2000').map(lambda x:(x[1], x[2], x[3], x[-1]))
rdd_q_2.foreach(print)
print('*' * 50)

# 3. rating above 4 name,year,rating,duration
rdd_q_3 = rdd.map(lambda x:x.split(',')).filter(lambda x: x[3] > '4').map(lambda x:(x[1], x[2], x[3], x[-1]))
rdd_q_3.foreach(print)
print('*' * 50)

# 4. Rating min 2 moives name, year, rating,duration
rdd_q_4 = rdd.map(lambda x:x.split(',')).filter(lambda x: x[3] > '3.5' and x[2]>'2005').map(lambda x:(x[1], x[2], x[3], x[-1]))
rdd_q_4.foreach(print)
print('*' * 50)