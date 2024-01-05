from pyspark.sql import SparkSession
from pyspark.sql.functions import *

ss = SparkSession.builder.master("local[1]").appName('jan').getOrCreate()  # local[1] for 1 master

# nested_list
neste_list = [[101, 'amal', 'nr', 34, 45, 45],
              [102, 'arjun', 'cd', 34, 25, 35],
              [103, 'rahul', 'bf', 45, 32, 23],
              [104, 'baby', 'vf', 34, 23, 24],
              [105, 'suman', 'mv', 34, 35, 34], ]
# column name
col_name = ['id', 'f_name', 'l_name','sub1','sub2','sub3']
df = ss.createDataFrame(data=neste_list, schema=col_name)
df.show(0)  # default 20 rows
df.show(3)
# colname -> luminar
df1 = df.withColumn('institute', lit('Luminar'))
df1.show(5)
# total mark
df2 = df1.withColumn('total_marks', col('sub1')+col('sub2')+col('sub3'))
df2.show()
# rename f_name to first_name
df3 = df2.withColumnRenamed('f_name','first_name')
df3.show()