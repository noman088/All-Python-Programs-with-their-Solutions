# 8. Write a python script to calculate sum of digits of a given number
s = 0

a = str(input("Enter a number"))
for i in a:
    s = s+(int(i))

print(s)
