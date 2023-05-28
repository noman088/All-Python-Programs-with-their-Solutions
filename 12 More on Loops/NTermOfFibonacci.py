# 8. Write a python script to print first N terms of a Fibonacci series
n=(int(input("Enter a Number ")))
a=-1
b=1
d=0

while d<n:
    c=a+b
    print(c)
    a=b
    b=c
    d+=1

