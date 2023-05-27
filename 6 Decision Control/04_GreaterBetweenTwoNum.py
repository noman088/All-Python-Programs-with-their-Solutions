# 4. Write a python script to print greater between two numbers. Print number only once
# even if the numbers are the same.

# a=int(input("Enter first Number"))
# b=int(input("Enter second Number"))
# if a>b:
#     print(a,"is greater")
# if b>a:
#     print(b,"is greater")
# else:
#     print(a)

print("enter two numbers")
a,b=int(input()),int(input())
print(a if a>b else b)

