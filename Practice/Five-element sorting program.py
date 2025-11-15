import numpy as np
arr = np.array([0]*5,int)
for i in range(len(arr)):
    arr[i]=int(input("Enter a number: "))
print("Before sorting")
print(arr)
arr.sort(axis=0,kind="quicksort",order=None)
print("after sorting")
print(arr)