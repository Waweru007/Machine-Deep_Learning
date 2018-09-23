height=[12,14,15,16,17,12,13,15,19,20]
weight=[60,50,40,50,47,58,70,60,50,80]
height
weight
height=[12,14,15,16,17,12,13,15,19,20]
weight=[60,50,40,50,47,58,70,60,50,80]
np.mean(npheight)
np.mean(npweight)
import numpy as np

npheight=np.array(height)
npweight=np.array(weight)


BMI=npheight/npweight**2
print(BMI)

#####List
xy=height+weight
print(xy)

BMI>0.004

####2D Array
hw=[[12,14,15,16,17,12,13,15,19,20],[60,50,40,50,47,58,70,60,50,80]]
hw=np.array(hw)
np.mean(hw[:,0])
np.corrcoef(hw[:,0],hw[:,1])
