# 5. Write a python script to find next prime number of a given number
n = int(input("Enter a Number"))
a=n+1
while 1:
    i = 2
    if (a % i == 0):
        a+=1
    else:
        print(a)
        break
    


