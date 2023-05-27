# 6. Write a python program to check whether a given string is a multiword string or single

a = str(input("Enter a String"))
flag = 0
for e in a:
    if (e == ' '):
        flag += 1
        break
match flag:
    case 0:
        print("String is  singleword String")
    case _:
        print("String is  multiword String")
