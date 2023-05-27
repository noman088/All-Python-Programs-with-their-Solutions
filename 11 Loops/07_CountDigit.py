# 7. Write a python script to count digits in a given number
count=0
# a=str(input("Enter a number"))
# for i in a:
#     count+=1
# print(count)
a=int(input("Enter a Number"))
while a:
    count+=1
    a= a//10

print(count)