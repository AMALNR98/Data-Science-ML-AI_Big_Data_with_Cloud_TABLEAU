***Matplotlib tutorials***
---
```python
import matplotlib.pyplot as plt
import numpy as np

# plot a line
x = [1, 2, 3, 5, 4, 2, 5, 6, 8]
y = [3, 4, 5, 6, 7, 3, 4, 7, 4]
plt.plot(x, y)
plt.show()
```
- ***Plot points***
```python
plt.plot(x, y, "*") # *, o, +, s, d, D, p(pentogon), H(Hexogon),
plt.show()
```
- ***plot an array***
```python
x1 = np.array([1,2,3,8,5])
y1 = np.array([1,5,3,6,3])
plt.plot(x1, y1)
plt.show()
```

---
- plot with single axis
 - it will act as y-axis
 - x-axis is automatically genereated
```python
x2 = np.array([3,5,3,2,6,4,3])
plt.plot(x2)
plt.show()
```
```python
plt.plot(x2, 'o')
plt.show()
```
- Plot line and points
```python
plt.plot(x2, marker = "s")
plt.show
```
---
---
Plot points with doted lines and selcet color
 - lines : solid, doted, dashed
 - colors: b,r,g,b,m,y
```python
ypoint = np.array([1,5,2,3])
plt.plot(ypoint, '*:g')
```
```python
# Dashed line
plt.plot(ypoint, '*--g')
```
- Change size of marker
```python
ypoints_1 = np.array([3,5,3,1,3])
plt.plot(ypoints_1, marker = 'o',ms = 20)
plt.show()
```
- Change color of marker edge
```python
plt.plot(ypoints_1,marker = 'o', ms = 10, mec = 'b') # mec = marker edge color
```
- Change face color
```python
plt.plot(ypoints_1,marker = 'o', ms = 10, mfc = 'hotpink') # we can use RGB code
```
- To change style of line
```python
# linestyle
plt.plot(ypoints_1, linestyle = 'dashed')# dashed, dotted, solid
```
- To change line width
```python
plt.plot(ypoints_1,linewidth = 10) # only integers will work
```
- To plot multiple
```python
x1 = [1,2,3,4]
x2 = [3,4,5,2]
x3 = [5,2,4,2]
x4 = [1,2,3,5]
plt.plot(x1,x2)
plt.plot(x3,x4)
```
---
- ***To show title, x-axis and y-axis***
```python
x = [150,160,156,176,189]
y = [53,56,59,66,79]
plt.plot(x,y)
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')
plt.title("Height-Weight Graph")
```
---
- ***Creating class using dictionary for font class***
```python

x = [150,160,156,176,189]
y = [53,56,59,66,79]
plt.plot(x,y)
font1 = {'family':'serif','color':'blue', 'size':20}
font2 = {'family':'serif','color':'red', 'size':10}

plt.xlabel('Height in cm', fontdict = font2)
plt.ylabel('Weight in kg', fontdict = font2)
plt.title("Height-Weight Graph", fontdict = font1)
```
---
****GRID****
```python
x = [150,160,156,176,189]
y = [53,56,59,66,79]
plt.plot(x,y)
font1 = {'family':'serif','color':'blue', 'size':20}
font2 = {'family':'serif','color':'red', 'size':10}

plt.xlabel('Height in cm', fontdict = font2)
plt.ylabel('Weight in kg', fontdict = font2)
plt.title("Height-Weight Graph", fontdict = font1)
#Grid
plt.grid()
```
- ***grid axis defining***
```python
x = [150,160,156,176,189]
y = [53,56,59,66,79]
plt.plot(x,y)
font1 = {'family':'serif','color':'blue', 'size':20}
font2 = {'family':'serif','color':'red', 'size':10}

plt.xlabel('Height in cm', fontdict = font2)
plt.ylabel('Weight in kg', fontdict = font2)
plt.title("Height-Weight Graph", fontdict = font1)
plt.grid(axis = 'x')
```
---
Grid style
```python
x = [150,160,156,176,189]
y = [53,56,59,66,79]
plt.plot(x,y)
font1 = {'family':'serif','color':'blue', 'size':20}
font2 = {'family':'serif','color':'red', 'size':10}

plt.xlabel('Height in cm', fontdict = font2)
plt.ylabel('Weight in kg', fontdict = font2)
plt.title("Height-Weight Graph", fontdict = font1)
plt.grid(color = 'green',linestyle = "--", linewidth = 1)
```
---
***Sub Plot***
```python
# 19 oct 23
x1 = [1, 2, 3, 4]
y1 = [3, 7, 5, 6]
plt.xlabel("Height in cm")
plt.ylabel('Weitht in kg')
plt.title("Height - Weight Graph")
plt.subplot(1, 2, 1) #(value 1 = row, value 2 = column, value 3 = position)(when value 1 and value 2 :- 1 row 2 column)
plt.plot(x1, y1)

x2 = [4, 6, 5, 2]
y2 = [3, 1, 4, 2]
plt.xlabel("Veleocity")
plt.ylabel('Time')
plt.title("Velocity - Time Graph")
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.suptitle('Graphs')
```
- ***Scatter Plot***
```python
x1 = [1, 2, 3, 4]
y1 = [4,2,5,1]
plt.scatter(x1,y1)
```
- ***Scatter plot for multiple graph***
```python
x1 = [1, 2, 3, 4]
y1 = [4,2,5,1]
plt.scatter(x1,y1)

x2 = [3,4,5,7]
y2 = [1,7,4,2]
plt.scatter(x2,y2)
```
---
***Bar Chart***
```python
x1 = [1, 2, 3, 4]
y1 = [3,4,5,6]
plt.bar(x1,y1)
```
---
***bar plot horizontal***
```python
x1 = [1, 2, 3, 4]
y1 = [3,4,5,6]
plt.barh(x1,y1, color = 'red')
```
---
- ***Histogram***

```python 
x = [1,1,2,2,2,3,3,3,3,4,4,4,4,4]#(1- 2 times, 2 - 3 times, 3 - 4 times, 4 - 5 times)
```
plt.hist(x)
---
- ***pychart***
- ```python
y = [ 3, 5,3,2]
my_label = ['apple','ornage', 'mango', 'grape'] # label for each item
plt.pie(y, labels = my_label)

plt.legend() # it display the labels parameter box
```