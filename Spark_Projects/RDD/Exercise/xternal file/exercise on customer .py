from pyspark import SparkContext
sc = SparkContext(master='local',appName='may').getOrCreate()
customer = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/customer1.txt')
customer.foreach(print)
