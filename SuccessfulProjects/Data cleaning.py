
import pandas as pd 
train=pd.read_csv('C:/Users/Wesh/Desktop/train.csv', index_col='Id')
data=pd.read_csv('E:/data1/dta/weka2.csv')
data.tail()
##show the columns 
train.columns.values
# Show the shape
train.shape
##show information about the data
data.info()
# Show that there is NaN data (Age,Fare Embarked), that needs to be handled during data cleansing
train.isnull().sum()

  # Create dammies
df1=pd.get_dummies(data['class'], prefix='class')
df1.head()

df =data.drop('class', axis=1)
df
##join the dammy to the df
df2= df.join(df1)   

df2.head() 

###Tranform the variable 
df3=data['class'].map( {'Normal': 1, 'Abnormal': 0} ).astype(int)
df3

train2=train.drop([f for f in train.columns if train[f].dtype !='object'], axis=1)
train2.head()

 
#read the dataset and sample 25% of it
loan = pd.read_csv('loan.csv').sample(frac = .25)


