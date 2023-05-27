# 12. Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part


# num = complex(input("Enter a Complex Number "))
# real = num.real
# imaginary = num.imag
# if real > imaginary:
#     print("real part is greater")
# if imaginary > real:
#     print("imaginary part is greater")
num=complex(input("enter a complex number"))
print((num.real) if num.real >num.imag else (num.imag))
