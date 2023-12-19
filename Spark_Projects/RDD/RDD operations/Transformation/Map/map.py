from pyspark import SparkContext
sc = SparkContext(master='local',appName='may')
rdd = sc.parallelize(([i for i in range(1,11)]))
rdd.foreach(print)

# map
