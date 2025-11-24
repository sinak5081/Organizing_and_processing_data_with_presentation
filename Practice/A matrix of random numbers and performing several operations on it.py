'''
1 = Printing matrix elements with loops
2 = Printing elements on the main diameter
3 = Printing elements on the minor diameter
4 = The sum of the elements of each individual row
5 = The sum of the elements of each individual column
'''
from matmodule import *
r = 3
c = 5
mat = np.matrix([([0] * c)for i in range(r)])
generator(mat)
print("Original matrix")
printMat(mat)
print("_______________________________________")
print("The element on first diagonal")
firstDiagonal(mat)
print("_______________________________________")
print("the element on second diagonal")
secDiagonal(mat)
print("_______________________________________")
print("sum of Rows")
print("_______________________________________")
SumofRows(mat)
print("_______________________________________")
print("Sum of columns")
print("_______________________________________")
sumofcols(mat)

