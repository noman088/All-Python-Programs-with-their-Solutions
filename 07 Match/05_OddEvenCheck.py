# 5. Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.

num = int(input("Enter a Number"))
if num > 0:
    if num % 2 == 0:
        print("Saurabh Shukla")
    elif num % 2 != 0:
        print("Aditya Chaudhry")

if num < 0:
    if num % 2 != 0:
        print("Prateek Jain")
