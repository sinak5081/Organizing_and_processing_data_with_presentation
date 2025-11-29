#Project description
"""
1. A prisoner has 20 solitary confinement cells. The lock on each cell door has the property that by turning the key once, its state changes; from closed to open and from open to closed. The following two methods are used to release the prisoners, and finally, the door that remains open releases that prisoner. The first method is that the doors are numbered. Doors with multiples of 1 are turned once, multiples of 2 twice, multiples of 3, etc., and multiples of 200 are turned two hundred times.
The second method is that the doors are numbered. Doors with multiples of 1 are turned once, multiples of 2 once, multiples of , once, etc., and multiples of 200 are also turned once.
In both methods, determine which doors will remain open to free the prisoners in those cells.
"""
import numpy as np 
import math
#Number of cells
n = 20
#First method
doors = np.zeros(n,dtype=int)
for step in range(1,n+1):
    for i in range(step-1,n,step):
        doors[i]=1-doors[i]
for index in range(n):
    if doors[index]== 1:
        print(index + 1)
print(doors)
#Second method
open_doors = []
for i in range(1,int(math.sqrt(n))+1):
    open_doors.append(i*i)
for doors in open_doors:
    print(doors)
print("Opened cells:")
print(open_doors)