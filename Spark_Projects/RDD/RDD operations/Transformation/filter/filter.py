# syntax
# new_rdd = old_rdd.filter(condition)


# 1 to 20 even numbers

from pyspark import SparkContext

sc = SparkContext(master='local', appName='may').getOrCreate()
rdd = sc.parallelize(([i for i in range(1, 21)]))
# even
even = rdd.filter((lambda x: x % 2 == 0))
even.foreach(print)
