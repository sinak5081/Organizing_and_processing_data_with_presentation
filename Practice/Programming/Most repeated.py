import numpy as np
n = int(input("How many numbers do you want to enter?:"))
arr = np.empty(n,dtype=int)
for i in range(len(arr)):
    arr[i] = int(input("Enter a number:"))
values,counts = np.unique(arr , return_counts=True)
max = counts.argmax()
print("array is:")
print(arr)
print("most repeted:",values[max],"count:",counts[max])
