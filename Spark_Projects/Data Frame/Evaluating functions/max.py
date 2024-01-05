"""
syntax:
    new_df = old_df.groupby('col_name').max('col_name')
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

ss = SparkSession.builder.master("local[1]").appName('jan').getOrCreate()  # local[1] for one master
df = ss.read.csv('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/customer1.txt',
                 sep=',', header=False, inferSchema=True).toDF('id', 'f_name', 'l_name', 'age', 'prof', 'loc')
# inferSchema is for correct datatype
df.show()