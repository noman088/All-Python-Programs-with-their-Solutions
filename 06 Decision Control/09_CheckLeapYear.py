# 9. Write a python script to check whether a given year is a leap year or not.
year=int(input("Enter a Year"))
if(year%100 ==0 and year%400 ==0) or (year%4==0 and year%100!=0):
    print(year," is a Leap year")
else:
    print(year,"is not a Leap Year")

