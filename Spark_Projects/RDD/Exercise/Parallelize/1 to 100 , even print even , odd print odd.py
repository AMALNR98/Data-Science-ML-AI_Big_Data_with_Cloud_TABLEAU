from pyspark import SparkContext
sc = SparkContext(master='local',appName='may')
rdd = sc.parallelize((i, 'even') if i % 2 == 0 else (i, 'odd') for i in range(1, 101))
rdd.foreach(print)