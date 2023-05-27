# 10. Write a program to display day name on the basis of user’s liking of a colour. Ask
# user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display
# day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday
a = str(input("Enter your Favoriout Colour \nEnter Like: i like this colour "))
print()
if a == "i like yellow colour":
    x = 1
elif a == "i like blue colour":
    x = 2
elif a == "i like orange colour":
    x = 3
elif a == "i like white colour":
    x = 4
elif a == "i like black colour":
    x = 5
elif a == "i like red colour":
    x = 6
else:
    x = 7

match x:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
