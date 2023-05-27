# 4. Write a program which takes user’s age and display the category of person. Age
# below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen.
age = int(input("Enter Your Age"))
if age < 20:
    print("Your are Teen")
elif 20 < age < 40:
    print("You are Young Man")
elif 40 < age < 60:
    print("You are Exprieced")
else:
    print("You are Senior Citizen")
