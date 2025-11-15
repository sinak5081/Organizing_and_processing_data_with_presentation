import numpy as np
arr = np.arange(10)
arr[3]=15
print("print select number:")
print("a[1]=",arr[1],"a[3=]",arr[3])
print("print arraye by for loop")
for item in arr:
    print(item,end=" ")
print("\nprint complete number")
print(arr)