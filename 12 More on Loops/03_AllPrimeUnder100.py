# 3. Write a python script to print all Prime numbers under 100
n=1
while n<=100:
    j=n//2
    i=2
    while i<=j:
        if n%i==0:
            break
        i+=1
    else:
        print(n,end=" ")
    n+=1

    