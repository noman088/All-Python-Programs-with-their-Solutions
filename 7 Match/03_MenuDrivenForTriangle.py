
import math
# 3. Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right
# angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.
while (1):
    a = int(input("Press 1 for continue \n Press 0 for Quit"))
    if a == 1:
        a = int(input("Enter first Number "))
        b = int(input("Enter Second Number "))
        c = int(input("Enter third Number "))
        print

        if a == b or a == c or b == c:
            x = 1
        elif a**2 == b**2+c**2 or b**2 == a**2+c**2 or c**2 == b**2+a**2:
            x = 2
        elif a == b == c:
            x = 3
        else:
            x = 4
        match x:
            case 1:
                print("This is Isosceles Triangle")
                print()

            case 2:
                print("This is Right Angle Triangle")
                print()
            case 3:
                print("This is Equilateral Triangle")
                print()
            case 4:
                print("Wrong Input ")
                print("Press 1 for try Again")
                print()
    if a == 0:
        exit()
