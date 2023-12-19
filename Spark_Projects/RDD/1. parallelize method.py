from pyspark import SparkContext
sc = SparkContext(master='local',appName='may').getOrCreate()
rdd = sc.parallelize([1,2,3,4,5,6,7])
rdd.foreach(print)