# group and count
# Syntax
# new_rdd = old_rdd/reduceByKey(condition)

# Wordcount
from pyspark import SparkContext

sc = SparkContext(master='local', appName='may').getOrCreate()
rdd = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/sample 1')
rdd.foreach(print)
print('*' * 50)

rdd1 = rdd.flatMap((lambda x: x.split(' ')))
rdd1.foreach(print)
print('*' * 50)

rdd2 = rdd1.map(lambda x: (x, 1))
rdd2.foreach(print)
print(('*' * 50))
# ('i', 1)
# ('am', 1)
# ('amal', 1)
# ('i', 1)
# ('am', 1)
# ('learning', 1)
# ('bigdata', 1)
# ('python', 1)
# ('bigdata', 1)
# ('spark', 1)
# ('machine', 1)
# ('learning', 1)
rdd3 = rdd2.reduceByKey(lambda x, y: x + y)
rdd3.foreach(print)
# ('i', 2)
# ('am', 2)
# ('amal', 1)
# ('learning', 2)
# ('bigdata', 2)
# ('python', 1)
# ('spark', 1)
# ('machine', 1)
print(('*' * 50))


# count by ascending order
rdd4 = rdd3.sortBy(lambda x:x[1],ascending=False)
rdd4.foreach(print)
print(('*' * 50))
