"""
1. Age mxm 2 employee fname, lname, age, phno
2. Age min 1 employee fname,lname. age
3. Chennai work age mxm one employee fname, lname, age
"""
from pyspark import SparkContext

sc = SparkContext(master='local', appName='may').getOrCreate()
rdd = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/sample4.txt')
rdd.foreach(print)
print('*' * 50)

rdd1 = rdd.map(lambda x: x.split(',')).sortBy(lambda x:x[3],ascending=False).map(lambda x:(x[1],x[2],x[3],x[4]))
rdd1.foreach(print)
lst = rdd1.take(2)
print(lst)
print('*' * 50)

rdd2 = rdd.map(lambda x: x.split(',')).sortBy(lambda x:x[3],ascending=True).map(lambda x:(x[1],x[2],x[3],x[4]))
rdd2.foreach(print)
lst1 = rdd2.take(1)
print(lst1)
print('*' * 50)

rdd3 = rdd.map(lambda x:x.split(',')).filter(lambda x:x[-1]=='Chennai').sortBy(lambda x:x[3],ascending=False)
rdd3.foreach(print)
lst2 = rdd3.first()
print(lst2)
print('*' * 50)