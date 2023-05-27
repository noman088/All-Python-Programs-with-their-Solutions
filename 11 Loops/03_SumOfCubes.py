# 3. Write a python script to calculate sum of cubes of first N natural numbers
s = 0
for i in range(int(input("Enter a number"))):
    s = s+((i+1)**3)
print(s)
