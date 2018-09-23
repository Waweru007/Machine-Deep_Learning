import pandas as pd
url1 = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1273/datasets/df1.csv'
url2 = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1273/datasets/df2.csv'
url3 = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1273/datasets/messy.csv'

df1 = pd.read_csv(url1, sep = ',')
df2 = pd.read_csv(url2, sep = ',')
messy = pd.read_csv(url3, sep=',')

print(df1)

#####################Reading and writing CSV
data=pd.read_csv('C:\\Users\\Wesh\\Desktop\\creditcard.csv')
data
#####Wtite
data.to_csv('C:\\Users\\Wesh\\Desktop\\Nw.csv',sep=',')

result=df[(df['Age']>30) &(df['sex']=='female')]results.to_excel('results.xlsx')

###3GET A GLIMPSE OF THE DATA
##########Summary stats
df1.describe()

###Check whether there are missing values
pd.isnull(df1).any()
x=df.isnull().any().sum()
x

y=df.isnull().sum()
y

###Drop any missign values

df1.dropna()
###Isolating certain groups
df1[df1['dogs']>2]

df1[df1['owner']=='Lisa']

df1[(df1['owner']=='Lisa') &(df1['cats']>8)]

#############Loading a new dataset

df


print(df2)
print(messy)
df2melt=pd.melt(df2,id_vars=['Country'])
print(df2melt)
df2tidy = df2melt.rename(columns = {'variable': 'Year', 'value': 'Income'}, inplace =False)
print(df2tidy)
dftidy = df2melt.rename(columns = {'variable': 'Year', 'value': 'Income'})
print(dftidy)


###DROPING COLUMNS
xy=df1.drop(["dogs"], axis=1)
xy
###Drop rows with index 1
xyz=df2.drop([1])
print(xyz)

###Drop all Duplicates 
df2melt.drop_duplicates(['Country'])

###Replace 1 with 7 in the whole dataset
df2melt.replace('Y1980','1980')
###Rename index 0 to zero

df2melt.rename(index={0:'zero'})



# Drop the columns where all elements are missing values:
df.dropna(axis=1, how='all')

# Drop the columns where any of the elements are missing values
df.dropna(axis=1, how='any')

# Keep only the rows which contain 2 missing values maximum
df.dropna(thresh=2)

# Drop the columns where any of the elements are missing values
df.dropna(axis=1, how='any')

# Fill all missing values with the mean of the particular column
df.fillna(df.mean())

# Fill any missing value in column 'A' with the column median
df['A'].fillna(df['A'].median())

# Fill any missing value in column 'Depeche' with the column mode
df['Depeche'].fillna(df['Depeche'].mode())

+# Drop the columns where all elements are missing values:
+df.dropna(axis=1, how='all')
+
+# Drop the columns where any of the elements are missing values
+df.dropna(axis=1, how='any')
+
+# Keep only the rows which contain 2 missing values maximum
+df.dropna(thresh=2)
+
+# Drop the columns where any of the elements are missing values
+df.dropna(axis=1, how='any')
+
+# Filling all missing values with the mean of the particular column
+df.fillna(df.mean())
+
+# Fill any missing value in column 'A' with the column median
+df['A'].fillna(df['A'].median())
+
+# Fill any missing value in column 'Depeche' with the column mode
+df['Depeche'].fillna(df['Depeche'].mode())



######saving data

