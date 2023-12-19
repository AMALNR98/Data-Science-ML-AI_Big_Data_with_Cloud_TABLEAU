from pyspark import SparkContext
sc = SparkContext(master='local',appName='may')
rdd = sc.parallelize(([(i, i**2) for i in range(1, 31) if i % 2 == 0]))
rdd.foreach(print)