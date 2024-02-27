from sklearn.neighbors import KNeighborsClassifier

# from example 2
# input columns
x1 = [7, 7, 3, 1]
x2 = [7, 4, 4, 4]

# output column
target = ['bad', 'bad', 'good', 'good']
print(x1)
print(x2)
# p1 (7,7) (7,4) (3,4) (1,4)
# for combine x1 and x2 like above use zip function
# and convert it into a list
features = list(zip(x1, x2))
print(features)

# model creation
knn = KNeighborsClassifier(n_neighbors=3)  # defining k's value as 3
# training model using fit function
knn.fit(features, target)  # training model

# predicting data
# here, we have only 4 input data, here all data taken for training,
# so there is no testing data because of limited data
print(knn.predict([[3, 7]]))
