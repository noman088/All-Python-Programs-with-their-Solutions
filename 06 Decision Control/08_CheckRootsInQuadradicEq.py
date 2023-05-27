
# 8. Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots

import math
a=int(input("Enter value of first coefficient"))
b=int(input("Enter value of second coefficient"))
c=int(input("Enter value of third coefficient"))
D=b**2-4*a*c

if D<0:
    print("Imaginary roots")
if D==0:
    print("Real & Equal Roots")
    root=-b/(2.0*a)
    print(root)
if D>0:
    print("there are two roots : Real & Distict  ")
    root1=(-b-math.sqrt(D))/2*a
    print('first is',root1)
    root2=(-b+math.sqrt(D))/2*a
    print('second is ',root2)


