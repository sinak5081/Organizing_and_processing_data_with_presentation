import numpy as np
# create a matrix with dimensions 2*2
x = np.matrix(((2,3),(3,5)))
print(x)
#create a matrix with dimensions 3*5
y = np.matrix([([0]*3) for i in range(5)])
print(y)
#_________________________
#Matrix addition and subtraction
a = np.matrix([[3,8],[4,6]])
print(a)
b = np.matrix([[4,0],[1,3]])
print(b)
print("Result of matrix iS:")
print(a+b)
#______________________________________
#Multiplication in matrices
c = np.matrix([[1,2,3],[4,5,6]])
print(c)
d = np.matrix([[7,8],[9,10],[11,12]])
print(d)
print("result of matrix m multiplication:")
print(c*d)
#____________________________________
#Matrix transposition
e = np.matrix([[6,4,5],[1,7,3]])
et = e.T
print(et)