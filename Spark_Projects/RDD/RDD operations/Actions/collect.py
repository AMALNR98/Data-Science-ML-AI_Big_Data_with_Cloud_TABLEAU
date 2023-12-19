from pyspark import SparkContext

sc = SparkContext(master='local', appName='may')
rdd1 = sc.parallelize(([i for i in range(1, 21)]))
rdd1.foreach(print)
print('*' * 100)

# Collect() ---> python list
lst = rdd1.collect()
print(lst)
