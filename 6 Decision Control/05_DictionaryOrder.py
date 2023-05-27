# # 5. Write a python script to print two given words in dictionary order
# a=str(input("Enter a Name"))
# b=str(input("Enter Second Name"))
# if a<b:
#     print(a,b)
# if a>b:
#     print(b,a)
print("Enter two string")
a,b=input(),input()
print((b,a) if a>b else (a,b))