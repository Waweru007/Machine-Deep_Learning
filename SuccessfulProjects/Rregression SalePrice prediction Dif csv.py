import matplotlib.pyplot as plt
from sklearn import datasets 
from sklearn import metrics 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
import pandas as pd

train=pd.read_csv("C:/Users/Wesh/Desktop/train.csv")
test=pd.read_csv("C:/Users/Wesh/Desktop/test.csv")
test
train
df=train.set_index(['YrSold','Street'])
df.head()
df.to_csv('C:\\Users\\Wesh\\Desktop\\SalePrice.csv',sep=',')
trtest=pd.concat([train, test], ignore_index=True)
trtest.describe()
trtest
