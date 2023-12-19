"""
Customer
1. India works and age above 50 fname,lname,age4, prof
2. UK work full data
3. US data and age above 50 fname, lname, age, prof
4. Each profession count [Count desc order]
5. Each location count [count desc]
"""
from pyspark import SparkContext

sc = SparkContext(master='local', appName='dec').getOrCreate()
rdd = sc.textFile(
    '/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/customer1.txt')
rdd.foreach(print)
print('*' * 50)

# 4. Each profession count [Count desc order]
rdd_split = rdd.map(lambda x: x.split(','))
rdd_key = rdd_split.map(lambda x: (x[4], 1))
rdd_key.foreach(print)
print('*' * 50)
rdd_Q_4 = rdd_key.reduceByKey(lambda x, y: x + y)
rdd_Q_4.foreach(print)
print('*' * 50)

# 3. US data and age above 50 fname, lname, age, prof
rdd_3_filter = rdd_split.filter(lambda x: x[-1] == 'us' and '25' < x[3] <= '40')
rdd_3_filter.foreach(print)
print('*' * 50)
