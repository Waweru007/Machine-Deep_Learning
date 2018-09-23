import matplotlib.pyplot as plt
from sklearn import datasets 
from sklearn import metrics 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
import pandas as pd
train=pd.read_csv("C:/Users/Wesh/Desktop/data.csv")
train.head()

###drop the variable SalePrice in the set of indepedent variables
x=train.drop('SalePrice', axis=1)
y=train.SalePrice

###split our data set so that we can test our accuracy
X_train, X_test, y_train, y_test=train_test_split(x,y, test_size=0.30, random_state=16)
##define the model to be used 
model=LinearRegression()
model.fit(X_train, y_train)

predictions=model.predict(X_test)
print(predictions)
plt.scatter(y_test,predictions)

#Rsquared
print(model.score(X_test,y_test))
print(metrics.mean_squared_error(y_test,predictions))

train3.to_csv('C:\\Users\\Wesh\\Desktop\\New.csv',sep=',')

