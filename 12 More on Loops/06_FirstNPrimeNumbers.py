# 6. Write a python script to print first N prime numbers
num = int(input("Enter a Number"))
a = 1
i = 2
while a <= num:
    while i<a:
        if(a%i==0):
            a+=1
            break
        i+=1
    else:
        print(a)
    
