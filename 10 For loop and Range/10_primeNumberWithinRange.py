# 10. Write a python script to display all prime numbers within a range.
# # range
# start = 15
# end = 45

a = range(15, 45, 1)
for i in a:
    j = 2
    k = i//2
    while j <= k:
        if (i % j == 0):
            break
        j += 1
    else:
        print(i)
