# 8. Write a python script to print squares of first N natural numbers

n = int(input("Enter a Number"))
i = 1
while i <= n:
    print(i*i, end=',')
    i += 1
