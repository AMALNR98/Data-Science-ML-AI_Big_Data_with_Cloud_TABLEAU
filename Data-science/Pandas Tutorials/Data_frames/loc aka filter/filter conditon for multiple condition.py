# Syntax

# new_data_frame_name = old_data_frame.loc[(old_data_frame_name['column_name']conditon) & (old_data_frame_name['column_name']condition)]

# age above 23 and loc Chennai

import pandas as pd

sample_4 = pd.read_csv('/home/amal/Downloads/sample4.txt', header=None)
sample_4.columns = ['id', 'fname', 'lname', 'age', 'phone_no', 'loc']
print(sample_4)
print("*" * 100)

sample_4_age_above_23_and_loc_chennai = sample_4.loc[(sample_4['age'] > 23) & (sample_4['loc'] == 'Chennai')]
print(sample_4_age_above_23_and_loc_chennai)
