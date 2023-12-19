from pyspark import SparkContext

sc = SparkContext(master='local', appName='may')
core = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/RDD operations/spark core.txt')
sql = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/RDD operations/spark sql.txt')
streaming = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/RDD operations/spark streaming.txt')
mlib = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/RDD operations/mlib.txt')


# 1.Each file wordcount [count desc order]
core_map = core.flatMap((lambda x: x.split(' ')))
core_map.foreach(print)
print('*' * 50)
core_foreach = core_map.map(lambda x: (x, 1))
core_foreach.foreach(print)
print(('*' * 50))
core_count = core_foreach.reduceByKey(lambda x, y: x + y).sortBy(lambda x:x,ascending=False)
core_count.foreach(print)
print(('*' * 50))

sql_map = sql.flatMap((lambda x: x.split(' ')))
sql_map.foreach(print)
print('*' * 50)
sql_foreach = sql_map.map(lambda x: (x, 1))
sql_foreach.foreach(print)
print(('*' * 50))
sql_count = sql_foreach.reduceByKey(lambda x, y: x + y).sortBy(lambda x:x,ascending=False)
sql_count.foreach(print)
print(('*' * 50))

streaming_map = streaming.flatMap((lambda x: x.split(' ')))
streaming_map.foreach(print)
print('*' * 50)
streaming_foreach = streaming_map.map(lambda x: (x, 1))
streaming_foreach.foreach(print)
print(('*' * 50))
streaming_count = streaming_foreach.reduceByKey(lambda x, y: x + y).sortBy(lambda x:x,ascending=False)
streaming_count.foreach(print)
print('*' * 50)

mlib_map = mlib.flatMap((lambda x: x.split(' ')))
mlib_map.foreach(print)
print('*' * 50)
mlib_foreach = mlib_map.map(lambda x: (x, 1))
mlib_foreach.foreach(print)
print(('*' * 50))
mlib_count = mlib_foreach.reduceByKey(lambda x, y: x + y).sortBy(lambda x:x,ascending=False)
mlib_count.foreach(print)
print('*' * 50)

# 2.Combine world count
total_word_count = core_count.union(mlib_count).union(streaming_count).union(sql_count)
total_word_count.foreach(print)