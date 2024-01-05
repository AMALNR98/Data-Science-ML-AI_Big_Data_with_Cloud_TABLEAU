from pyspark.sql import SparkSession
from pyspark.sql.functions import *

ss = SparkSession.builder.master("local[1]").appName('jan').getOrCreate()  # local[1] for one master
df = ss.read.csv('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/sample4.txt', sep=',', header=False, inferSchema=True).toDF('id', 'f_name', 'l_name','age','mob_no','loc')
# inferSchema is for correct datatype
df.show()
print(df.printSchema())

"""
1. Age above 23, fname,lname, age,phon
2. Age equal to 21 fname, lname, age
3. chennai work fname, lname, age,,phno
4. chennai work and age above 23 fname,lname, age
"""
df1 = df.filter(col('age')>23).select(col('f_name'),col('l_name'),col('age'),col('mob_no'))
df1.show()
df2 = df.filter(col('age')==21).select(col('f_name'),col('l_name'),col('age'),col('mob_no'))
df2.show()
df3= df.filter(col('age')>23) and (col('loc')=='Chennai').select('f_name','l_name','age')
df3.show()