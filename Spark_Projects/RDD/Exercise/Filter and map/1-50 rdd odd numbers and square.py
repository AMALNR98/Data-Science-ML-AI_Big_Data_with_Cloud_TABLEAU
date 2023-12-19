from pyspark import SparkContext
sc = SparkContext(master='local',appName='dec').getOrCreate()
rdd = sc.parallelize([i for i in range(1,51)])
rdd1 = rdd.filter(lambda  x:x%2 == 0 and x%5==0)
rdd1.foreach(print)