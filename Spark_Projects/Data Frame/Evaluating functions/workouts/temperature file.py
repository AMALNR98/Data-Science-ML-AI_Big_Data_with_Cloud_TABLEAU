from pyspark.sql import SparkSession
from pyspark.sql.functions import *

ss = SparkSession.builder.master("local[1]").appName('jan').getOrCreate()  # local[1] for one master
df = ss.read.csv('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/files/temper',
                 sep=',', header=False, inferSchema=True).toDF('district','temp')
# inferSchema is for correct datatype
df.show()

# Each district maximum temp:
max_temp = df.groupBy('district').max('temp')
max_temp.show()

min_temp = df.groupBy('district').min('temp') \
    .orderBy('max(temp)', ascending=False)
min_temp.show()

avg_temp = df.groupBy('district').avg('temp') \
    .orderBy('avg(temp)', ascending=False)
avg_temp.show()