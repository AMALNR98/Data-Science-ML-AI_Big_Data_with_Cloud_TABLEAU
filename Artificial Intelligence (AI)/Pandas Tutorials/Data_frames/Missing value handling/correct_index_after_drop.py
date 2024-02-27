# new_dataframe_name = old_data_frame_name.dropna(ignore_index=true)
import pandas as pd

missing_data1 = pd.read_csv(
    '/home/amal/Downloads/missing_data1.csv')
print(missing_data1)
print(missing_data1.shape)

drop_row = missing_data1.dropna(ignore_index=True)
print(drop_row)
print(drop_row.shape)

# or reset_index

reset = missing_data1.reset_index()
print(reset)
print(reset.shape)