import numpy as np
def update(stArr):
    for i in range(len(stArr)):
        if stArr[i] <= 19:
            arr[i] += 1
arr = np.zeros(5,float)
for i in range(len(arr)):
    arr[i] = float(input("Enter an avrage: "))
print("Before update")
print(arr)
update(arr)
print("After update")
print(arr)