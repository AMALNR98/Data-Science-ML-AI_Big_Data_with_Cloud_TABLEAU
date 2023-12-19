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
rdd1 = rdd.map(lambda x: x.startswith('i'))
rdd1.foreach(print)
# Output will be
# True
# True
# False
# False
# False
# False


