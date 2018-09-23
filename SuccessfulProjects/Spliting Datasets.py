import numpy as np
import pandas as pd

Y=(1,2,4,5,6,7,8,14,19,10)
X=(12,13,14,15,16,17,18,19,20,21)
split_percentage=0.7
split=int(split_percentage*len(Y))
Y_train=Y[:split]
Y_test=Y[split:]
X_train=X[:split]
X_test=X[split:]
print(Y_test)
print(Y_train)
print(X_test)
print(X_train)

###Method Two This one is random(Best)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X,Y, test_size=0.3,random_state=2)
print(Y_test)
print(Y_train)
print(X_test)
print(X_train)
