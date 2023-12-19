from pyspark import SparkContext

sc = SparkContext(master='local', appName='may')
rdd = sc.parallelize(([i for i in range(1, 21)]))
rdd.foreach(print)

# map

# Syntax: new_rdd = old_rdd.map(condition)

# Add 6 to all elements in rdd

rdd_add_6 = rdd.map(lambda x: x + 6)
rdd.foreach(print)
print('*' * 50)
# 1-10 elements square
rdd1 = sc.parallelize(([i for i in range(1, 30)]))
square_rdd = rdd.map(lambda x: (x, x ** 2))  # PAIR RDD
square_rdd.foreach(print)
print('*' * 50)

# 1-30 print even number for even and odd vise versa
rdd2 = sc.parallelize(([i for i in range(1, 50)]))
odd_or_even = rdd2.map(lambda x: (x, 'even') if x % 2 == 0 else (x, 'odd'))
odd_or_even.foreach(print)
print('*' * 50)

# 1 to 50 rdd and print 1-15 -> small, 16-35 element -> medium, above 35 is larger
rdd_size = rdd2.map(lambda x: (x, 'small') if x < 16 else (x, 'medium') if 15 <= x < 35 else (x, 'large'))
rdd_size.foreach(print)
