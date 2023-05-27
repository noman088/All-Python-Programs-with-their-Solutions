# 2. Write a menu driven program to perform following operations - Addition, Subtraction,
# Multiplication, Division
while (1):

    print()
    print("Press the Number You want to follow")
    print(" 1. Addition")
    print(" 2. Substraction")
    print(" 3. Multiplication")
    print(" 4. Division ")
    print(" 0. Exit ")
    x = int(input())
    match x:
        case 1:
            a=int(input("Enter first Number "))
            b=int(input("Enter second Number "))
            c=a+b;
            print( "Answer is :  ",c)
        case 2:
            a=int(input("Enter first Number "))
            b=int(input("Enter second Number "))
            c=a-b;
            print( "Answer is :  ",c)
        case 3:
            a=int(input("Enter first Number "))
            b=int(input("Enter second Number "))
            c=a*b;
            print( "Answer is :  ",c)
        case 4:
            a=int(input("Enter first Number "))
            b=int(input("Enter second Number "))
            c=a//b;
            print( "Answer is :  ",c)
        case 0:
            exit()
        
            
