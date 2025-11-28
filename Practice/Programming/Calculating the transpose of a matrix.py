import numpy as np 
arr = np.zeros((3,5),float)
for i in range(3):
    for j in range(5):
        arr[i,j]=float(input("Enter number:"))
print("The transliteration is equal to:")
print(arr.T)