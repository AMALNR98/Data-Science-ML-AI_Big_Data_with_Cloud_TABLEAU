from pyspark import SparkContext

sc = SparkContext(master='local', appName='dec').getOrCreate()
rdd = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/sample 1')
rdd.foreach(print)

print("*" * 50)
rdd1 = rdd.flatMap(lambda x: x.split(' '))
rdd1.foreach(print)

rdd2 = rdd1.map(lambda x:(x,1))
data = rdd2.countByKey()

print(data)