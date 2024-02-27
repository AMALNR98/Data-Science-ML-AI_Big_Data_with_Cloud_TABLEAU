# drop missing value included row
# new_data_frame_name = old_data_frame_name.dropna()
import numpy as np
import pandas as pd

missing_data1 = pd.read_csv(
    '/home/amal/Downloads/missing_data1.csv')
print(missing_data1)
print(missing_data1.shape)

drop_row = missing_data1.dropna()
print(drop_row)
print(drop_row.shape)