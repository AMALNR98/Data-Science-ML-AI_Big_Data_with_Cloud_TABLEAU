from pyspark import SparkContext
sc = SparkContext(master='local',appName='dec').getOrCreate()
sample4 = sc.textFile('/home/amal/Documents/Data-Science-ML-AI_Big_Data_with_Cloud_TABLEAU/Spark_Projects/RDD/sample4.txt')
sample4.foreach(print)
print('*'*50)
# split
rdd1 = sample4.map(lambda x:x.split(','))
rdd1.foreach(print)
print('*'*50)

# collect data of age above 23
age_above_23 = rdd1.filter(lambda  x:x[3]>'23')
age_above_23.foreach(print)
print('*'*50)

# collect wanted columns
wanted_columns = rdd1.map(lambda x:(x[1],x[2],x[4]))
wanted_columns.foreach(print)
print('*'*50)

# ///////////////////////////////////////////////////
#age above 24 fname,lname, age, phoneno
age_above_24_f_l_age_ph = rdd1.map(lambda x:x[3] > '23' and (x[1],x[2],x[4]))
age_above_24_f_l_age_ph.foreach(print)
print('*'*50)

# Chennai work fname,lname, age, phno
chennai = rdd1.map(lambda x:x[5] == 'Chennai' and (x[1],x[2],x[4]))
chennai.foreach(print)
print('*'*50)

# age above 23 and loc chennai fname, lname, age, phno
age_and_location = rdd1.map()
age_and_location.foreach(print)
print('*'*50)
