"""
txn.txt
..................
1. Find Row count
2. jan month oid,cusno,category,product,state
A. Row count
3. July Month oid,cusno,category,product,state
B. Row count
4. Each category [count desc sort]
5. Category full deatils
6. Each paymethod count
7. jan-july month purchase count [include]
8. Each category total amount
9. Each category maximum amount
10. Each category avg amount
11.total amount by cash and credit card
12. Indoor games ,total amount
13. Each state count
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

ss = SparkSession.builder.master("local[1]").appName('jan').getOrCreate()  # local[1] for one master
df = ss.read.csv('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/files/txn.txt',
                 sep=',', header=False, inferSchema=True).toDF('id', 'date', 'cus_no','amount','category','product', 'loc', 'state', 'payment_method')
df.show(5)

print('1. Find Row count')
row_count = df.count()
print(row_count)

print('*'*50)
print('2. jan month oid,cusno,category,product,state')
question_2_a = df.filter(col('date').contains('01-'))
question_2 = question_2_a.filter(~col('date').contains('-01-')).select(col('cus_no'),col('category'),col('product'),col('state'))
question_2.show()

print('*'*50)
print('2.A. Row count')
question_2_A = question_2.count()
print(question_2_A)

print('*'*50)
print('3. July Month oid,cusno,category,product,state')
question_3_a = df.filter(col('date').contains('06-'))
question_3 = question_3_a.filter(~col('date').contains('-06-')).select(col('cus_no'),col('category'),col('product'),col('state'))
question_3.show()

print('*'*50)
print('3.B. Row count')
question_3_A = question_3.count()
print(question_3_A)

print('*'*50)
print('4. Each category [count desc sort]')
question_5 = df.groupBy('category').count().orderBy('count',ascending = False)
question_5.show()

print('*'*50)
print('5. Category full deatils')
question_5_A = df.groupBy('category').count().orderBy('count',ascending = False)
question_5_A.show()

print('*'*50)
print('6. Each paymethod count')
question_6 = df.groupBy('payment_method').count().orderBy('count',ascending = False)
question_6.show()

print('*'*50)
print('7. jan-july month purchase count [include]')

print('*'*50)
print('8. Each category total amount')
question_8 = df.groupBy('category').sum('amount')
question_8.show()

print('*'*50)
print('9. Each category maximum amount')
question_9 = df.groupBy('category').max('amount')
question_9.show()

print('*'*50)
print('10. Each category avg amount')
question_10 = df.groupBy('category').avg('amount')
question_10.show()

print('*'*50)
print('11.total amount by cash and credit card')
question_11 = df.groupBy('payment_method').sum('amount')
question_11.show()


print('*'*50)
print('12. Indoor games ,total amount')
question_12 = df.groupBy('category').sum('amount')
indoor_games_total_amount = question_12.filter(col('category')=='Indoor Games')
indoor_games_total_amount.show()

print('*'*50)
print('13. Each state count')
question_13 = df.groupBy('state').count()
question_13.show()