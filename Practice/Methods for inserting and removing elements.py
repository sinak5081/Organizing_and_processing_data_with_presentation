import numpy as np
#method append:This method adds values ​​to the end of the array.
a = np.array([[1,3],[5,7],[8,9]],dtype=int)
b = np.array([[1,2,3,4,5,6,7,8,9,10]],dtype=int)
print(a)
print("adding new value to the end of columns ")
print(np.append(a,[[10,11],[12,13]],axis=0))
print("adding new value to the end of row ")
print(np.append(b,[[11,12,13,14]],axis=1))
print("___________________________________________________")
#__________________________________________________________
#method insert:This method inserts values ​​into a specific location in the array.
print(a)
print("inserting new value in second line:")
print(np.insert(a,2,[20,30],axis=0))
print(b)
print("___________________________________________________")
#_________________________________________________________
#method delete:This method deletes part of the array.
c = np.arange(10).reshape(5,2)
print(c)
print("delete Eighth line:")
print(np.delete(c,3,axis=0))
print("___________________________________________________")
#_________________________________________________________
#method vstack:Vertically joins two or more arrays.
# method hstack:Joins two or more arrays horizontally.
c = np.array([[1,2],[3,4]])
e = np.array([[5,6],[7,8]])
print("Vertically joins array")
print(np.vstack((c,e)))
print("arrays horizontally:")
print(np.hstack((c,e)))
print("___________________________________________________")
#_________________________________________________________
#method split:This method is used to divide an array into multiple parts.
g = np.array([[1,2,3,4,5,6,7,8,9]])
print("first array")
print(g)
print("split array to 3 section")
print(np.split(g,3,axis=1))
print("split using 1-d array")
print(np.split(g,[2,7],axis=1))