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
###Deviding datasets 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.3,random_state=21,stratify=y)

####Use randomForestRegressor for regression problem
from sklearn.ensemble import RandomForestClassifier

##Create Random Forest Object

model=RandomForestClassifier(n_estimators=1000)

####Train the Model using the training sets and check
model.fit(x_train,y_train)

###Predict Output

predicted= model.predict(x_test)

###Score
print("Test Set Predictions:\n {}".format(y_test))
model.score(x_test,y_test)
