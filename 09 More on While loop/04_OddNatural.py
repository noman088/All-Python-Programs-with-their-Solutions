# 4. Write a python script to print first N odd natural numbers

n = int(input("Enter a Number"))
i = 1
while i <= n:
    print(2*i-1, end=" ")
    i += 1
