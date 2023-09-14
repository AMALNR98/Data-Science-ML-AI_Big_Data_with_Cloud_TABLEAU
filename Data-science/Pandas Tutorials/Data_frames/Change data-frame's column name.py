import numpy as np
import pandas as pd

sample_4 = pd.read_csv(
    '/home/amal/Downloads/sample4.txt',header=None)  # if the file is comma separation there is no need to define
print(sample_4)
sample_4.columns=['id','first_name','last_name','age','phone_number','location']
print("*" * 100)
print(sample_4)
# rename
#new_data_frame_name = old_data_frame_name(columns={'old_column_name':'new_colnamn_name')}

