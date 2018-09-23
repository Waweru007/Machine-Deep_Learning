
 ####Timer Programs in python 
import os
import time


s=0
m=0

while s<=60:
    os.system('cls')
    print (m, 'Minutes', s, 'Seconds')
    time.sleep(1)
    s+=1
    if s==60:
        m+=1
        s=0
 
########Count down from 2 minutes 
import os
import time
for t in range(120,-1,-1):
    minutes = t / 60
    seconds = t % 60
    print("%d:%2d" % (minutes,seconds))# Python v2 only
    time.sleep(1.0)