from pyspark import SparkContext
sc = SparkContext(master='local',appName='may')
rdd = sc.parallelize(([i for i in range(1,101) if i % 2 == 0]))
rdd.foreach(print)