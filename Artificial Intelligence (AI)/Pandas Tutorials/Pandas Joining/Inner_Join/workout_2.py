import numpy as np
import pandas as pd

student = pd.read_csv('/home/amal/Downloads/student', header=None)
student.columns = ['name', 'id']
print(student)
print("*" * 100)
result = pd.read_csv('/home/amal/Downloads/results', header=None)
result.columns = ['id', 'result']
print(result)

# result
# .........
# roll, res

# pass name, roll, res
inner_joined_data = pd.merge(student, result, on='id', how='inner')[['name', 'id', 'result']]
print(inner_joined_data)
