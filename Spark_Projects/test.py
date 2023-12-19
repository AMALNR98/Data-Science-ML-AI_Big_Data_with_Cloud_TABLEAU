from pyspark import SparkContext
sc = SparkContext(master='local',appName='dec').getOrCreate()
rdd = sc.parallelize([1,2,3,4,5,6])
rdd.foreach(print)
