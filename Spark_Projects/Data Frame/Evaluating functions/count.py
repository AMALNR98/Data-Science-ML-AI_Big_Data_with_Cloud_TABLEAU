"""
Syntax:
    new_df = old_df.group('col_name').count('col_name')
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

ss = SparkSession.builder.master("local[1]").appName('jan').getOrCreate()  # local[1] for one master
df = ss.read.csv('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/customer1.txt',
                 sep=',', header=False, inferSchema=True).toDF('id', 'f_name', 'l_name', 'age', 'prof', 'loc')
# inferSchema is for correct datatype
df.show()
print('*' * 50)
"""##########Count#############"""
df_count = df.groupBy('loc').count()
df_count.show()
print('*' * 50)

# 1.customer each profession count count desc
profession_count = df.groupBy('prof').count().orderBy('count', ascending=False)
profession_count.show()
print('*' * 50)

# 2. Each location count count desc
location_count_desc = df.groupBy('loc').count().orderBy('count', ascending=False)
location_count_desc.show()
print('*' * 50)

# Works in india each profession count
works_in_india = df.filter(col('loc') == 'india') \
    .groupBy('prof').count() \
    .orderBy('count', ascending = False)
works_in_india.show()