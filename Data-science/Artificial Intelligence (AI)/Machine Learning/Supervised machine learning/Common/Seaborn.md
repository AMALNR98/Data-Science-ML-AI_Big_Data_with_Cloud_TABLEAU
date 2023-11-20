- ***Seaborn**
```python
import seaborn as sns
df = sns.load_dataset('tips') # In seaborn there are lot of datasets for practice
df
```
---
- ***Tutorials***
**Corelation(corr)**
--
- it find how the dependent variable relatated to independend variable.
- lower values is 0 and higher values is 1(0-1)
- conditons
  ---
  - Both columns should be numerical(Cant find on strings)
```python
df.corr()
```
- ***Heat map***
--
- representing correlation in graphically (Heatmap)
```python
sns.heatmap(df.corr())
```

***Joint Plot***
---
- Like scatter plot with histogram
- In x independent variable and in y dependent variable
```python
sns.jointplot(x = 'total_bill', y = 'tip', data = df, kind = 'reg') # kind = 'reg' is to plot regression line
```
```python
sns.jointplot(x = 'total_bill', y = 'tip', data = df, kind = 'hex') # kind = 'hex' hexgon plot
```
**Pair Plot**
--
```python
sns.pairplot(df)
sns.pairplot(df)
df['sex'].value_counts()
df['day'].value_counts()
df['time'].value_counts()
sns.pairplot(df,hue='sex') # differenciate male and female customers
```
**Count Plot**
--
- we can count and plot data
```python
sns.countplot(x= 'sex',data = df)
sns.countplot(x= 'day',data = df)
```
- **When we use y-axis for data and x-axis for count**
```python
sns.countplot(y = 'sex',data = df)
```
- ***count plot and hue***
```python
sns.countplot(x= 'sex',data = df, hue = 'smoker')
```
**Bar Plot**
--
```python
sns.barplot(x= 'total_bill', y = 'sex', data = df)
sns.barplot(x= 'total_bill', y = 'day', data = df)
```
- ***Box Plot***
---
A box plot, also known as a box-and-whisker plot, is a graphical representation of the distribution of a dataset. Seaborn makes it easy to create box plots to visualize the summary statistics of a dataset, including the median, quartiles, and any potential outliers.
- The box represents the interquartile range (IQR), with the lower and upper quartiles (25th and 75th percentiles) defining its edges.
- The horizontal line inside the box represents the median (50th percentile).
- The "whiskers" extend from the edges of the box to the minimum and maximum values within 1.5 times the IQR from the quartiles.
- Any data points beyond the whiskers are considered potential outliers and are plotted individually.
```python
sns.boxplot(y = 'total_bill', x = 'smoker', data = df)
```
-Percentile calculation example:
--
3, 5, 7, 1, 1, 8, 4, 6
1. Sort data accending order
  - 1, 1, 3, 4, 5, 6, 7, 8
2. Find median
  - 1, 1, 3, 4   5, 6, 7, 8
  - Median : 4+5/2 = 4.5 (**q2 or 50 percentile**)
3. Find **q1 or 25 percentile** =
    - 1, 1,  3, 4
    - q1 = 1 +3 / 2 = 2
4. Find **Q3 or 75 percentile**
    - 5, 6, 7, 8
    - q3 = 6 + 7 / 2 = 6.5
7. Find ***IQR (Inter Quartile Range)***
    - ``IQR = Q3 - Q1``
    - iqr = 6.5 - 2.4 = 4.5
    - ``Top outliers = Q3 = 1.5 * IQR``
    - 6.5 + 1.5 * 4.5 = 13.25
    - ``Bottum outliers = Q1 - 1.5 * IQR``
    - 2 - 1.5 * 4.5 = -4.75