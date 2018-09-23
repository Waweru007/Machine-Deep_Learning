#Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import decomposition
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
import seaborn as sb
%matplotlib inline
from sklearn import metrics 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split



 ##EXPLAROTARY DATA ANALYSIS 
import pandas as pd 
train=pd.read_csv('C:/Users/Wesh/Desktop/train.csv', index_col='Id')
train.head()
train.tail()

##show the columns 
train.columns.values
# Show the shape
train.shape

train.info()



train1=train.drop([f for f in train.columns if train[f].dtype =='object'], axis=1)

train1.head()

# Show that there is NaN data (Age,Fare Embarked), that needs to be handled during data cleansing
train1.isnull().sum()

# Drop the columns where any of the elements are missing values
train2=train1.dropna(axis=1, how='any')

# Show the shape
train2.shape

###STANDARDIZATION 
 import sklearn
 from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
print(scaler.fit(train2))
StandardScaler(copy=True, with_mean=True, with_std=True)
print(scaler.mean_)

std_train=scaler.transform(train2)
std_train
std_train.shape
 #we have 20 features

covar_matrix = PCA(n_components = 20)
covar_matrix.fit(std_train)
variance = covar_matrix.explained_variance_ratio_ #calculate variance ratios

var=np.cumsum(np.round(covar_matrix.explained_variance_ratio_, decimals=3)*100)

#We have created one Variable Var 
var 

##PLoting our One variable 
plt.ylabel('% Variance Explained')
plt.xlabel('# of Features')
plt.title('PCA Analysis')
plt.ylim(21,89)
plt.style.context('seaborn-whitegrid')

plt.plot(var)

###Based on the plot above it's clear we should pick 17 features
##because it is the maximum point of our graph 
y=train2.SalePrice
m=train2.drop(['SalePrice'], axis=1)
###We drop collumns to remain with 17 indepedent variables 
x=m.iloc[:,0:16] 
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
