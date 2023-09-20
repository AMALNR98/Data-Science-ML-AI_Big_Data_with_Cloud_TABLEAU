# new_dat_frame = old_data_farm_name.groupby('column_name') ['column_name].min

import numpy as np
import pandas as pd

temperature = pd.read_csv('/home/amal/Downloads/temper', header=None)
temperature.columns = ['district', 'temp']
print(temperature)
print("*" * 150)

# max
# new_data_frame_name = old_data_frame_name.groupby('column_name') ['column_name'].max()

max_temp = temperature.groupby('district') ['temp'].min()
print(max_temp)
