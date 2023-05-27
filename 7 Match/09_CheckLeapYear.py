
# 9. Write a python script to check whether a given year is
# a. Non century leap year
# b. Century leap year
# c. Non century non leap year
# d. Century non leap year
year = int(input("Enter a Year "))
if year%4==0 and (year %100!=0 or year%400==0):
    if year%100==0:
        print("Year is Century Leap Year")
    else:
        print("Year is Non Century Leap Year")
else:
    if year%100==0:
        print("Year is Century Non-Leap Year")
    else:
        print("Year is non Century nor Leap Year")
    