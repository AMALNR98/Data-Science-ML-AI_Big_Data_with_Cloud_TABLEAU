# line by line data convert into word by word
# 1-D word by word

# Syntax:
# new_rdd = old_rdd.flatMap(condition)

from pyspark import SparkContext

sc = SparkContext(master='local', appName='may').getOrCreate()
rdd = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/sample 1')
rdd.foreach(print)
print('*' * 50)

# i am amal
# i am learning bigdata
# python
# bigdata
# spark
# machine learning

rdd1 = rdd.map(lambda x: x.split(' '))
rdd1.foreach(print)
print('*' * 50)
# ['i', 'am', 'amal']
# ['i', 'am', 'learning', 'bigdata']
# ['python']
# ['bigdata']
# ['spark']
# ['machine', 'learning']
# **************************************************

rdd2 = rdd1.flatMap(lambda x: x)
rdd2.foreach(print)
print('*' * 50)
# i
# am
# amal
# i
# am
# learning
# bigdata
# python
# bigdata
# spark
# machine
# learning
# **************************************************

# We can do it directly from rdd
rdd3 = rdd.flatMap(lambda x:x.split(' '))
rdd3.foreach(print)