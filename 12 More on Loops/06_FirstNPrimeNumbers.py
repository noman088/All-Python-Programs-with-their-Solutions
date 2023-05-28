# 6. Write a python script to print first N prime numbers
a = int(input("Enter a number: "))
while a:
    i = 2
    j = 2
    while True:
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
        if flag == 0:
            print(i, end=" ")
            a -= 1
        if a == 0:
            break
        i += 1

print()
