import numpy as np
import pandas as pd

nested_list_1 = [[101, 'amal', 'nr', 25, 'bigdata', 1000],
                 [102, 'john', 'joseph', 24, 'python', 1000],
                 [104,'raju', 'k', 45, 'python', 1000],
                 [104, 'ram', 'ld', 35,'bigdata', 1000]]
print(nested_list_1)
print("*" * 150)
data_frame_1 = pd.DataFrame(nested_list_1, columns=['id','first_name','last_name','age','prof','salary'])
print(data_frame_1)

print(data_frame_1.head(2))
print(data_frame_1.tail(3))