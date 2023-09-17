import pandas as pd

sample_4 = pd.read_csv('/home/amal/Downloads/sample4.txt', header=None)
sample_4.columns = ['id', 'fname', 'lname', 'age', 'phone_no', 'loc']
print(sample_4)
print("*" * 100)

# new_data_frame_name = old_data_frame_name.loc[old_data_frame_name['column_name']condition]

# filtering age above 23

age_above_23 = sample_4.loc[sample_4['age'] > 23]
print(age_above_23)
print("*" * 100)

# age equal to 24, fname,lname, age,phone_no
age_above_24 = sample_4.loc[sample_4['age'] == 24].iloc[:,1:4]
print("*" * 100)

# chennai work ---> lname, lname, age, phone,loc
sample_4_Channai = sample_4.loc[sample_4['loc'] == 'Chennai'][['fname', 'lname', 'age', 'phone_no', 'loc']]
# sample_4_Channai = sample_4.loc[sample_4['loc'] == 'Chennai'].iloc[:, 1:5]        ---------------> using iloc
print(sample_4_Channai)
