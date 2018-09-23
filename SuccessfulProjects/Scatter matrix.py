import matplotlib.pyplot as plt
from sklearn import datasets 
from sklearn import metrics 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
import pandas as pd

###load the train dataset
train=pd.read_csv("C:/Users/Wesh/Desktop/train.csv")
##see the first five rows of the dataset
test=pd.read_csv("C:/Users/Wesh/Desktop/test.csv")
train.head()
test.head()

###define y
y=train.SalePrice
train1=train.drop(['SalePrice','Id'], axis=1)

##drop all the string variables
train2=train1.drop([f for f in train.columns if train[f].dtype =='object'], axis=1)
train2.head()
##assess missing variables 
missing=train2.isnull().sum()
missing

###drop columns with missing variables 
train3=train2.fillna(method='bfill')

###drop the variable SalePrice in the set of indepedent variables
x=train3
x

###split our data set so that we can test our accuracy
X_train, X_test, y_train, y_test=train_test_split(x,y, test_size=0.30, random_state=16)
##define the model to be used  and train
model=LinearRegression()
model.fit(x, y)
predictions=model.predict(X_test)
print(predictions)
plt.scatter(y_test,predictions)
plt.xlabel('Actaul Sale Prices')
plt.ylabel('Predicted Sale Prices')

plt.title('Predicted Against the Actual Sale Prices',y=1.05)

print(model.score(X_test,y_test))
##print(metrics.mean_squared_error(y_test,predictions))
##prepare test data 
##drop all the string variables
test1=test.drop([f for f in test.columns if test[f].dtype =='object'], axis=1)
test1.head()
##assess missing variables 
missing=test1.isnull().sum()
missing

###drop columns with missing variables 

test2=test1.drop(['LotFrontage','MasVnrArea','GarageYrBlt','Id'], axis=1)
##fill in missing values 
test3=test2.fillna(method='bfill')

##predict sales in test data set
predictions2=model.predict(test3)
print(predictions2)
plt.scatter(y_test,predictions)

