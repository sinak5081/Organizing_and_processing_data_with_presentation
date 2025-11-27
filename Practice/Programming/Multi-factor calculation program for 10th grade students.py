import numpy as np
#Average Grade
#Number of grades below the average Grade
#Number of grades up the average Grade

arr = np.zeros(10,float)
for i in range(len(arr)):
    arr[i]=float(input("Enter a 10th grade:"))
print(arr)
average = arr.mean()
print("average of grades:",average)
up = 0
Lower = 0
for i in range(len(arr)):
    if arr[i] > average:
        up += 1
print("Number of grades above the average grade point average:",up)
for i in range(len(arr)):
    if arr[i]<average:
        Lower += 1
print("Number of grades below the average grade point average: ",Lower)