import numpy as np
import pandas as pd

sample_4 = pd.read_csv(
    '/home/amal/Downloads/sample4.txt',header=None)  # if the file is comma separation there is no need to define
print(sample_4)
sample_4.columns=['id','first_name','last_name','age','phone_number','location']
print("*" * 100)
print(sample_4)
print("*" * 100)
sample_4_select = sample_4[['first_name','last_name','age']]        # don't forget to put double []
print(sample_4_select)