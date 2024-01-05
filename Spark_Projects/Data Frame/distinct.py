from pyspark.sql import SparkSession
from pyspark.sql.functions import *

ss = SparkSession.builder.master("local[1]").appName('jan').getOrCreate()  # local[1] for one master
df = ss.read.csv('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/sample4.txt', sep=',', header=False, inferSchema=True).toDF('id', 'f_name', 'l_name','age','mob_no','loc')
# inferSchema is for correct datatype
df.show()
print(df.printSchema())
df1= df.distinct()
df1.show()