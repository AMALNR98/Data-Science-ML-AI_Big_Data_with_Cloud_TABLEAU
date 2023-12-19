from pyspark import SparkContext
sc = SparkContext(master='local',appName='may').getOrCreate()
movies = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/movies.csv')
movies.foreach(print)