####Basic Read SPSS as pandas dataframe
import pandas as pd

import savReaderWriter as s
df= pd.DataFrame(list(s.SavReader('C:/Users/Wesh/Desktop/Data.sav')))
df.head()

df= pd.DataFrame(list(s.SavReader('C:/Users/Wesh/Desktop/Data.sav')))
df.describe()




####Read SPSS as a numpy array
import pandas as pd
import numpy as np
import savReaderWriter as s

with s.SavReaderNp ('C:/Users/Wesh/Desktop/Data.sav') as reader:
    records = reader.all()
df1 = pd.DataFrame(records)
df1.head()

df1.describe()
