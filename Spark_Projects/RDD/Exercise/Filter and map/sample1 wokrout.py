from pyspark import SparkContext
sc = SparkContext(master='local',appName='dec').getOrCreate()
sample1 = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/sample 1')
sample1.foreach(print)

# # filter data that stat with i
# rdd1 = sample1.filter(lambda x:x.startwith('i'))
# rdd1.foreach(print)

""" Exerciser
i [1]
am [1,0]
amal[1,0,1,0]
i
am learning

if there is vowel print 1 else 0
"""
sample = sample1.flatMap(lambda  x:x.split(' '))
sample.foreach(print)
vowels ='aeiouAEIOU'
# check_vowel_and_collect = sample.map(lambda x:[1 if i in vowels else 0 for i in x])
# check_vowel_and_collect.foreach(print)
check_vowel_and_collect = sample.map(lambda x:(x, [1 if i in vowels else 0 for i in x]))
check_vowel_and_collect.foreach(print)

# To count vowel
count_vowel_and_collect = sample.map(lambda x: (x, sum([1 if i in vowels else 0 for i in x])))
count_vowel_and_collect.foreach(print)

rdd3 = count_vowel_and_collect.filter(lambda x:x[1]>2)
rdd3.foreach((print)