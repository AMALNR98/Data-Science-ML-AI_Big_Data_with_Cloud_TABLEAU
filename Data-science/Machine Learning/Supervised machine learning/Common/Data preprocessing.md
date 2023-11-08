1. *** Drop ***
---
```python
train = train_data.drop(['Unnamed: 0'], axis = 1)
train
```
2. ***Count***
---
```python
train_data['Location'].value_counts()
```
3. ***Encoding Techniques***
---
- ***Label Recording***
---
```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

credit_score['Gender'] = le.fit_transform(credit_score['Gender'])
```
- ***One hot encoding***
---
  - get_dummies is in pandas library
```python
train_data_1 = pd.get_dummies(train_data[['Location','Fuel_Type','Transmission','Owner_Type']], drop_first = True) # drop_first is for drop first column (Here first column is name)
train_data_1

#Concatinate old dataframe and new dataframe

combined_data = pd.concat([train_data, train_data_1], axis=1)
combined_data
```
4. ***Remove String values***
```python
combined_data['Mileage'] = combined_data['Mileage'].str.replace('km/kg', '') # replace km/kg with 'non space'
combined_data['Mileage'] = combined_data['Mileage'].str.replace('kmpl', '')
combined_data
```
5. ***In this data set there is 'null' value as string (not null value). it's not missing value. So replace that null as zero***
---
```python
combined_data['Mileage'] = combined_data['Mileage'].str.replace('null','0')
```
6. ***Datatype conversion***
---
```python
combined_data['Mileage'] = combined_data['Mileage'].astype(float)
```
7. ***Replacing all zero values to missing value(NaN) using numpy***
---
```python
combined_data.loc[combined_data.Mileage == 0, 'Mileage'] = np.NaN
```
8.***Fill missing values***
---
```python
combined_data['Engine'] = combined_data['Engine'].fillna(combined_data['Engine'].mean())
```