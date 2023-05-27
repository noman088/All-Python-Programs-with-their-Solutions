# 10. Write a python script to print greater among three numbers. Print number only once
# even if the numbers are the same.

# a = int(input("Enter first Number"))
# b = int(input("Enter second Number"))
# c = int(input("Enter third Number"))
# if (a > b and a > c):
#     print(a," is greater")
# elif(b>a and b>c):
#     print(b," is greater")
# elif(c>a and c>b):
#     print(c," is greatest")
# else:
#     print("all are same")
#     print(a)

print("Enter three Numbers")
a,b,c=int(input()),int(input()),int(input())
print((a if a>c else c) if a>b  else (b if b>c else c) )