# 5. Write a python script to calculate sum of first N even natural numbers
s = 0
for i in range(int(input("enter a number"))):
    s = s+(2*(i+1)-1)
print("Sum of First N Even Number is ", s)
