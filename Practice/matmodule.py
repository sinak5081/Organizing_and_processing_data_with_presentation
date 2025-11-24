import numpy as np
import random
def generator(arr):
    for i in range(np.size(arr,0)):
        for j in range(np.size(arr,1)):
            arr[i, j] = random.randint(0, 99)
def printMat(arr):
    for i in range(np.size(arr,0)):
        for j in range(np.size(arr,1)):
            print("%3d" % arr[i,j],end= " ")
        print()
def firstDiagonal(arr):
    for i in range(np.size(arr,0)):
        for j in range(np.size(arr , 1)):
            if i == j :
                print("%3d" % arr[i,j],end=" ")
    print()
def secDiagonal(arr):
    for i in range(np.size(arr , 0)):
        for j in range(np.size(arr , 1)):
            if (i+j)==(np.size(arr ,1 ) - 1):
                print("%3d"%arr[i,j],end=" ")
    print()
def SumofRows(arr):
    print("Row     rowsum")
    for i in range(np.size(arr , 0)):
        Rsum = 0
        for j in range(np.size(arr,1)):
            Rsum += arr[i, j]
        print(i,"\t",Rsum)
def sumofcols(arr):
    print("col   colsum")
    for j in range(np.size(arr,1)):
        Csum = 0
        for i in range(np.size(arr,0)):
            Csum += arr[i, j]
        print(j,"\t",Csum)
        