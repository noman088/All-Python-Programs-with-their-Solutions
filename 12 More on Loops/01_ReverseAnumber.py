# 1. Write a python script to reverse a number.

a = int(input("Enter a number"))
s = 0
while a:
    s = (s*10)+a % 10
    a = a//10
print(s)
