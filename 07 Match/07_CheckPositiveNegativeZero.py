# 7. Write a python program to check whether a given number is positive, negative or
# zero using match case statement
a = int(input("Enter a Number"))
if a > 0:
    x = 1
if a < 0:
    x = 2
if a == 0:
    x = 0
match x:
    case 0:
        print("Number is zero")
    case 1:
        print("Number is Positive")
    case 2:
        print("Number is Negative")
