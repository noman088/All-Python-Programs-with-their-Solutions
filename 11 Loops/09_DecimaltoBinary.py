# 9. Write a python script to print binary equivalent of a given decimal number. (do not
# use bin() method)
a=int(input("Enter a number"))
n=[]

while a>0:
    digit =(a%2)
    n.append(digit)
    a//=2

n.reverse();
for e in n:
    print(e,end='')
    
