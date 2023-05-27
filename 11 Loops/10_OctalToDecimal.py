# 10. Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)
a=int(input("Enter a number "))
print()
n=[]
while a>0:
    digit=(a%8)
    n.append(digit)
    a//=8

n.reverse()
print("Octal of given decimal is ")
for e in n:
    print(e ,end="")