# 11. Write a python script to take the month value in numeric format and display the
# number of days in it.

# month=int(input("Enter Number of Month"))
# if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#     print("31 Days")
# if month==4 or month==6 or month==9 or month==11:
#     print("30 Days")
# if month==2:
#     print("28 OR 29 Days")
month = int(input("enter month number "))
if month in (1, 3, 5, 7, 8, 10, 12):
    print("31 Days")
elif month in (4, 6, 9, 11):
    print("30 Days")
elif month == 2:
    print("28 OR 29 Days")
else:
    print("Invalid Input")
