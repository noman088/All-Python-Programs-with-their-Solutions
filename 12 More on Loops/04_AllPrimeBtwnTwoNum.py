# 4. Write a python script to print all Prime numbers between two given numbers (both
# values inclusive)
a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))
while a <= b:
    j = a//2
    i = 2
    while i <= j:
        if (a % i == 0):
            break
        i += 1
    else:
        print(a)
    a += 1
