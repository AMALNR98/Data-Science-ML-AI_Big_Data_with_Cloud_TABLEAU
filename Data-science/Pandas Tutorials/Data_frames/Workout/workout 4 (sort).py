# sample4.txt
# 1. Age mxm 2 employee fname, lname, age, phone number
# 2. Age min 1 empoyee fname, lnaem, age, loc
# 3 Chennai work, age,  mxm 1 empoye fname, lname, age, phone_number

import numpy as np
import pandas as pd

sample_4 = pd.read_csv(
    '/home/amal/Downloads/sample4.txt', header=None)  # if the file is comma separation there is no need to define

sample_4.columns = ['id', 'first_name', 'last_name', 'age', 'phone_number', 'location']
# hierarchy
# sort
# select
# head
age_mxm_2_emp_f_l_a_p = sample_4.sort_values(by='age', ascending=False)[
    ['first_name', 'last_name', 'age', 'location']].head(2)
print(age_mxm_2_emp_f_l_a_p)
print("*" * 100)
age_min_1_emp_f_l_a_p = sample_4.sort_values(by='age') \
    [['first_name', 'last_name', 'age', 'location']].head(1)  # intention
print(age_min_1_emp_f_l_a_p)
print("*" * 100)

chennei_work_age_mxm_1_f_l_a_p = sample_4.loc[sample_4["location"] == "Chennai"] \
    .sort_values(by='age', ascending=False)[['first_name', 'last_name', 'age', 'location']].head(2)
print(chennei_work_age_mxm_1_f_l_a_p)
