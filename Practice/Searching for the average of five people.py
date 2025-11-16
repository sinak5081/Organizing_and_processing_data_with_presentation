import numpy as np
grades = np.zeros(5)
for i in range(len(grades)):
    grades[i] = int(input("Enter a grade: "))
print("arraye is:")
print(grades)
min = np.amin(grades,0)
max = np.amax(grades,0)
print("min is:",min,"max is :",max)
item = 20
x = np.where(grades == item)
if len (x[0]):
    print("number", item, "found at:",x[0])
else:
    print("number is not found")
