import numpy as np 
row_a = int(input("Enter row for matrix a: "))
col_a = int(input("enter col for matrix a: "))
a = np.zeros((row_a,col_a),float)
for i in range(row_a):
    for j in range(col_a):
        a[i,j]=float(input("Enter a number: "))

row_b=int(input("Enter Row for matrix b: "))
col_b=int(input("Enter a Col for matrix b: "))
b = np.zeros((row_b,col_b),float)
for i in range(row_b):
    for j in range(col_b):
        b[i,j]=float(input("Enter a number: "))

print("Matrix a: ")
print(a)
print("_________________")
print("Matrix b:")
print(b)
print("_______________")
def add_matrix(a,b):
    print("The sum of two matrix a and b:")
    print(a+b)
add_matrix(a,b)