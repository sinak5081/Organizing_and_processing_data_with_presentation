import numpy as np
#numpy.amax === Finds the maximum value.
a = np.array([1,2,10,4,5])
max =np.amax(a,axis=0)
print(max)
#______________________________________________
#numpy.amin==Finds the minimum value.
b = np.array([1,2,3,0,4,5])
min = np.amin(b,axis=0)
print(min)
#________________________________________________
#numpy.where==Finds the desired value.
c = np.array([20,30,100,40,54])
item = 54
x = np.where(c==item)
print(x[0])
