# 7. Write a python script to print first N even natural numbers in reverse order

n = int(input("Enter a Number "))
while n >= 1:
    print(2*n, end="\n")
    n -= 1
