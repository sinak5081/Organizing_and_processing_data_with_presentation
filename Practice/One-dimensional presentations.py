# first install numpy liberary
import numpy as np
#method zeros
a = np.zeros(10,int)
print(a)
#This method returns an array of length 10 and type int.
c = np.zeros(5)
print(c)
#This method returns an array of length 3 and type string
b=np.array([5 , 10 , 15])
print(b)
#This method returns an array of length 5 and value 5,10,15
t = np.array(['apple']*5,dtype=object)
print(t)
#This method returns an array of length 3 and value 1,2,3 and data type complex
e = np.array([1,2,3],dtype=complex)
print(e)
#This method returns an array of length 5 and value 1 and data type float,
f = np.array([1]*5,dtype=float)
print(f)