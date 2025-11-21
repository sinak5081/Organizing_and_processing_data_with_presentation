import numpy as np
#method zeros:Creates a two-dimensional array of type int with dimensions 5x3.
a = np.zeros((3,5),dtype=int,order="C")
print(a)
#____________________________________________________
#method array:Create a two-dimensional array with dimensions 2*3
b = np.array([[1,2,3],[4,5,6]])
print(b) 
#___________________________________________
#create array by for lop
c = np.array([([0]*3) for i in range(5)],order="F")
print(c)
#___________________________________________
#method empty:Creates a two-dimensional array of dimensions 3x2 whose elements are rows.
d = np.empty((2,3),order="C")
print(d)
#____________________________________________________
#method reshape:Converts a one-dimensional array to a two-dimensional one.
e = np.arange(8).reshape(2,4)
print(e)
#______________________________________________
#method ones:create two-dimensional array with dimensions 3*5 all of value equal to 1
f = np.ones((3,5),order="F")
print(f)
#__________________________________
#method random:create two-dimensional array with dimensions 3*3 with random value
g = np.random.random((3,3))
print(g)
#________________________________________________________
#method identity:Creates a square array with dimensions 3*3 and whose diameter is one and whose elements are all integers.
h = np.identity(3,dtype=int)
print(h)