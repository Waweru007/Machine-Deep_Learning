#Data Manipulation 
import numpy as np
import pandas as pd

#plotting

import matplotlib.pyplot as plt

##Mchine Learning
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

## Data fetching 
df=pd.read_csv('E:/dta/Google.csv')

df=df.dropna()
df=df[['Open','High','Low','Close']]
df.head()

#####Predictor Variables 
df['Open-Close']=df.Open-df.Close
df['High-Low']=df.High-df.Low
df.dropna()
X=df[['Open-Close','High-Low']]
X.head()

##Target Variable
Y=np.where(df['Close'].shift(-1)>df['Close'],1,-1)
print(Y)

##Split the Dataset
split_percentage=0.7
split=int(split_percentage*len(df))

X_train=X[:split]
Y_train=Y[:split]

X_test=X[split:]
Y_test=Y[split:]
##################OR===Split the Dataset(Randomly)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X,Y, test_size=0.3,random_state=10)

####KNN Learning Model (K=15)
knn=KNeighborsClassifier(n_neighbors=15)

##Fit the model

knn.fit(X_train,Y_train)

####Accuracy Score

accuracy_train=accuracy_score(Y_train,knn.predict(X_train))
accuracy_test=accuracy_score(Y_test, knn.predict(X_test))

print('Train_data Accuracy:%2f' %accuracy_train)
print('Test_data Accuracy: %.2f' %accuracy_test)

#####Predict Signal 
df['Predicted_Signal']=knn.predict(X)

###SPY Cumulative Returns
df['SPY_Returns']=np.log(df['Close']/df['Close'].shift(1))
Cumulative_SPY_Returns=df[split:]['SPY_Returns'].cumsum()*100

###Cumulative Strategey Returns 
df['Strategy_Returns']=df['SPY_Returns']* df['Predicted_Signal'].shift(1)
Cum_Strategy_Returns=df[split:]['Strategy_Returns'].cumsum()*100



#####Plot the results
plt.figure(figsize=(10,5))
plt.plot(Cumulative_SPY_Returns,Color='r',label='SPY Returns')
plt.plot(Cum_Strategy_Returns,color='g',label='Strategy Returns')
plt.legend
plt.show()

