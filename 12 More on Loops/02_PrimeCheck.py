# 2. Write a python script to check whether a given number is Prime or not

a=int(input("Enter a Number"))
j=a//2
i=2
while i<=j:
    if(j%i==0):
        print("Not Prime")
        break
    i+=1
else:
    print("Prime")
