# Remove duplicate rows(not elements)
from pyspark import SparkContext

sc = SparkContext(master='local', appName='dec').getOrCreate()
rdd = sc.textFile(
    '/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/customer1.txt')
rdd.foreach(print)
print('*' * 50)

# 4. Each profession count [Count desc order]
rdd_split = rdd.map(lambda x: x.split(','))


rdd_dist = rdd_split.distinct()