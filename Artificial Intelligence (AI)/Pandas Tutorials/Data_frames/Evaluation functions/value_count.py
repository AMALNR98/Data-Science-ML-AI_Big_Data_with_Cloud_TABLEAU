import numpy as np
import pandas as pd

sample_4 = pd.read_csv('/home/amal/Downloads/sample4.txt', header=None)
sample_4.columns = ['id', 'fname', 'lname', 'age', 'phone_no', 'loc']
print(sample_4)
print("*" * 150)
data_frame_1 = pd.DataFrame(sample_4)
print(data_frame_1)
print("*" * 150)

df1 = data_frame_1.groupby('loc') ['loc'].count()
print(df1)

df2 = data_frame_1.groupby('loc')
df3 = data_frame_1['loc'].value_counts()
print(df3)