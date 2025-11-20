from search_module import *
import numpy as np
arr = np.array([0]*5)
for i in range(len(arr)):
    arr[i]=int(input("Enter a student number:"))
item = int(input("Enter a number to search:"))
result = seqSearch(arr,item)
print("Result of sequential search:")
if result >= 0:
    print("value",item,"exist at position",result)
else:
    print("value",item,"not exist")
bubble(arr)
print("array after sorting: ")
print(arr)
print("result of binary search: ")
result = binSearch(arr,item)
if result >= 0:
    print("value",item,"exist is position",result)
else:
    print("value",item,"not exist")
