# 2. Write a python script to calculate sum of squares of first N natural numbers
s = 0
for i in range(int(input("Enter a number"))):
    s = s+((i+1)**2)
print(s)
