from sklearn import  datasets
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
iris=datasets.load_iris()
type(iris)
print(iris.keys())
type(iris.data)
iris.data.shape
print(iris.data)
print(iris.target)

x=iris.data
y=iris.target

#Part ONE
from sklearn.neighbors import KNeighborsClassifier 
knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(iris['data'],iris['target'])
X_new=pd.read_csv('C:/Users/Wesh/Desktop/X_new.csv')
prediction=knn.predict(X_new)
print('prediction{}'.format(prediction))

#Part TWO#Train Test Fuction 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.3,random_state=21,stratify=y)
from sklearn.neighbors import KNeighborsClassifier 
knn=KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)

print("Test Set Predictions:\n {}".format(y_pred))
knn.score(x_test,y_test)
