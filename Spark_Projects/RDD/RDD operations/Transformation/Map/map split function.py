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

# **************************************************
# ['i', 'am', 'amal']
# ['i', 'am', 'learning', 'bigdata']
# ['python']
# ['bigdata']
# ['spark']
# ['machine', 'learning']
