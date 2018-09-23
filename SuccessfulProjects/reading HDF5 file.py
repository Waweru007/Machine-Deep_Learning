import h5py 
import numpy as np
import pandas as pd

iris = pd.read_csv('C:/Users/Wesh/Desktop/creditcard.csv')

iris.to_hdf("iris.h5", "iris", index=False)
