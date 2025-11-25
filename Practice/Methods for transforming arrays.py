import numpy as np
#method Reshape:Converting a one-dimensional array to a two-dimensional one
a = np.arange(10)
print(a)
Reshape = np.reshape(a,(2,5))
print(Reshape)
print("__________________________________________________________________")
#___________________________________________________________________________
#method Resize:Used to change shape and size.
b = np.array([[0,1],[2,3]],order="c")
b.resize((2,3))
print(b)
resize = np.resize(a,(2,3))
print(resize)
print("__________________________________________________________________")
#___________________________________________________________________________
#method reval:Converting a multidimensional array to a single-dimensional one
c = np.array([[0,1],[2,3]],order="C")
print(c)
print(c.ravel('C'))