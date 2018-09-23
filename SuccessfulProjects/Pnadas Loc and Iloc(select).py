import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('C:/Users/Wesh/Desktop/uk.csv')
df

##set y to be the first 100 rows of the 4th column
y = df.iloc[0:10, 4].values
y
df['id'] = [random.randint(0,1000) for x in range(df.shape[0])]
##first row ""
df.iloc[0]
##last row
df.iloc[-1]

df.iloc[:,0] # first column of data frame (first_name)
df.iloc[:,1] # second column of data frame (last_name)
df.iloc[:,-1] # last column of data frame (id)
# Multiple row and column selections using iloc and DataFrame
df.iloc[0:5] # first five rows of dataframe
df.iloc[:, 0:2] # first two columns of data frame with all rows
df.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
df.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).
df1=df.set_index('last_name')
df1.head()
##Where index is Erm
df1.loc['Erm']

##loc to rows
df1.loc[['Erm','Veness']]

df1.loc[['Erm','Veness'],['first_name']]
df1.loc[['Erm','Veness'],'city':'email'] ##from city to email
# Select same rows, with just 'first_name', 'address' and 'city' columns
df.loc['Andrade':'Veness', ['first_name', 'address', 'city']]

df.set_index('id', inplace=True)
# select the row with 'id' = 487
df.loc[487]

# Select rows with first name Antonio, # and all columns between 'city' and 'email'
df1.loc[df1['first_name'] == 'Antonio', 'city':'email']

# Select rows where the email column ends with 'hotmail.com', include all columns
df.loc[df['email'].str.endswith("hotmail.com")] 

# Select rows with last_name equal to some values, all columns
df.loc[df['first_name'].isin(['France', 'Tyisha', 'Eric'])]  

# Select rows with first name Antonio AND hotmail email addresses
df1.loc[df1['email'].str.endswith("gmail.com") & (df1['first_name'] == 'Antonio')]   

# select rows with id column between 100 and 200, and just return 'postal' and 'web' columns
df.loc[(df['id'] > 100) & (df['id'] <= 200), ['postal', 'web']] 
 
# A lambda function that yields True/False values can also be used.
# Select rows where the company name has 4 words in it.
df.loc[df['company_name'].apply(lambda x: len(x.split(' ')) == 4)] 
 
# Selections can be achieved outside of the main .loc for clarity:
# Form a separate variable with your selections:
idx = df1['company_name'].apply(lambda x: len(x.split(' ')) == 4)
# Select only the True values in 'idx' and only the 3 columns specified:
df1.loc[idx, ['email', 'first_name', 'company']]

# Change the first name of all rows with an ID greater than 2000 to "John"
df.loc[df['id'] > 2000, "first_name"] = "John"

# Change the first name of all rows with an ID greater than 2000 to "John"
df.loc[df['id'] > 2000, "first_name"] = "John"