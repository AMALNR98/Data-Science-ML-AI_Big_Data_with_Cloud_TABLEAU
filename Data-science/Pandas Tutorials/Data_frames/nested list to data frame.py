import numpy as np
import pandas as pd


nested_list_1 = [[101, 'amal', 'nr', 25, 'bigdata', 1000],
                 [102, 'john', 'joseph', 24, 'python', 1000],
                 ['raju', 'k', 45, 'python', 1000],
                 [103, 'ram', 'ld', 35, '1000']]
print(nested_list_1)
print("*"*150)
data_frame_1 = pd.DataFrame(nested_list_1)
print(data_frame_1)