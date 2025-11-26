import numpy as np
# method sum:To calculate the sum of array elements
a = np.array([[2,4,6,8,10],[1,3,5,7,9]],dtype=int)
print(a)
print("sum of row:",a.sum(axis=1))
print("sum of columns:",a.sum(axis=0))
print("___________________________________________")
#_____________________________________________________
#method mean:Prints the average of the elements of an array.
print(a)
print("average of row:",a.mean(axis=1))
print("average of columns:",a.mean(axis=0))
print("___________________________________________")
#_____________________________________________________
#method var:Calculates the variance of the elements.
print(a)
print("variance of row:",a.var(axis=1))
print("variance of columns:",a.var(axis=0))
print("___________________________________________")
#_____________________________________________________
#method std:Calculating the standard deviation of an element on an axis
print(a)
print("standard of row:",a.std(axis=1))
print("standard of columns:",a.std(axis=0))
print("___________________________________________")
#_____________________________________________________
#method prod:Calculating the product of elements
print(a)
print("sum of product of row:",a.prod(axis=1))
print("sum of product of columns:",a.prod(axis=0))
print("___________________________________________")
#_____________________________________________________
#method size:Show the number of elements in the array.
print(a)
print("number of element of row:",np.size(a,axis=1))
print("number of element of columns:",np.size(a,axis=0))
print("___________________________________________")
#_____________________________________________________
#method copy:This method copies the array.
print(a)
b = a.copy()
print("copy the array in b:")
print(b)
print("___________________________________________")
#_____________________________________________________
#method median:This method calculates the median of the elements.
print(a)
print("median of row:",np.median(a,axis=1))
print("median of columns:",np.median(a,axis=0))