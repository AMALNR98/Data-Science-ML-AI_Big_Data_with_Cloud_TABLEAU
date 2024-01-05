from pyspark.sql import SparkSession
from pyspark.sql.functions import *

ss = SparkSession.builder.master("local[1]").appName('jan').getOrCreate()  # local[1] for 1 master

# nested_list
neste_list = [[101, 'amal', 2010, 24, 'python', 'ekm', 2050],
              [102, 'arjun', 2011, 25, 'spark', 'cal', 2150],
              [103, 'rahul', 2012, 26, 'big data', 'trs', 2250],
              [104, 'baby', 2013, 27, 'pandas', 'tsr', 2350],
              [105, 'suman', 2014, 24, 'python', 'tvm', 2450], ]
# column name
col_name = ['id', 'name', 'year', 'age', 'prof', 'loc', 'salary']
df = ss.createDataFrame(data=neste_list, schema=col_name)
df.show(0)  # default 20 rows
df.show(3)

'''Print dataframes column names'''
print(df.printSchema())
# root
#  |-- id: long (nullable = true)
#  |-- name: string (nullable = true)
#  |-- year: long (nullable = true)
#  |-- prof: long (nullable = true)
#  |-- loc: string (nullable = true)
#  |-- salary: string (nullable = true)
#  |-- _7: long (nullable = true)

'''row count'''
print(df.count())

'''How to add new columns into a data frame with constant value'''
df1 = df.withColumn('designation', lit('Software Engineer'))
# lit:- to give constant value to every row in added column
# for work lit we need to import pyspark.sql.functions
df1.show()
# +---+-----+----+----+--------+------+----+-----------------+
# | id| name|year|prof|     loc|salary|  _7|      designation|
# +---+-----+----+----+--------+------+----+-----------------+
# |101| amal|2010|  24|  python|   ekm|2050|Software Engineer|
# |102|arjun|2011|  25|   spark|   cal|2150|Software Engineer|
# |103|rahul|2012|  26|big data|   trs|2250|Software Engineer|
# |104| baby|2013|  27|  pandas|   tsr|2350|Software Engineer|
# |105|suman|2014|  24|  python|   tvm|2450|Software Engineer|
# +---+-----+----+----+--------+------+----+-----------------+
print('*'*50)
'''How to add new columns into a data frame'''
df2 = df1.withColumn('designation', lit('Software Engineer')) \
    .withColumn('bonus', col('salary')*0.10) \
    .withColumn('total salary', col('salary') + col('bonus')) \
    .withColumnRenamed('name', 'first_name')
df2.show()

''' How to drop a column'''
# df3 = df1.drop('designation')
# print(df3)
print('*'*50)

"""Drop multipel columns"""
df3 = df1.drop('designation','loc')
print(df3)
print('*'*50)
print('''How to select a column''')
'''How to select a column'''
df4 = df2.select('id','first_name','age','loc')
df4.show()
print('*'*50)

"""Filter"""
# Syntax
#   new_df = old_df.filter(col('col_name')condition)
df5 = df2.filter(col('age')>25)
df5.show()
print('*'*50)
# for multiple condition
df6 = df2.filter(col('age')>25) and (col('salary')>2150)
df6.show()


"""Sort()"""

df7 = df1.orderBy('age')
df7.show()