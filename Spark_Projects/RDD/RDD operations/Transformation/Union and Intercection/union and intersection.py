from pyspark import SparkContext

sc = SparkContext(master='local', appName='may')
rdd1 = sc.parallelize(([i for i in range(1, 21)]))
rdd1.foreach(print)
print('*'*50)
rdd2 = sc.parallelize(([i for i in range(10, 31)]))
rdd2.foreach(print)
print('*'*50)

# Union
rdd3 = rdd1.union(rdd2)
rdd3.foreach(print)
print('*'*50)

# Intersection
#     common elements in two RDDs
rdd4 = rdd1.intersection(rdd2)
rdd4.foreach(print)
print('*'*50)

# sort by ascending
rdd5 = rdd1.intersection(rdd2).sortBy(lambda x:x,ascending=False)
rdd5.foreach(print)
print('*'*50)
