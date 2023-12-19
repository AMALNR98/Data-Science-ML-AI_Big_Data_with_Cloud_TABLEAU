from pyspark import SparkContext

sc = SparkContext(master='local', appName='may')
rdd1 = sc.parallelize(([i for i in range(1, 21)]))
rdd1.foreach(print)
print('*' * 100)

# only take wanted elements to list
#   To collect the first four elements
lst = rdd1.take(4)
print(lst)
print('*' * 100)

# To collect first element
lst1 = rdd1.first()
print(lst1)
print('*' * 100)

