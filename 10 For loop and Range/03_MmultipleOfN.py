# 3. Write a python script to print first M multiples of N.
m = int(input("Enter how much time do you wanna print a number  "))
n = int(input("Enter the number  "))
x = range(1, m+1, 1)
for i in x:
    print(i*n, end=" ")
