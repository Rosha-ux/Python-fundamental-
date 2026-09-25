n= 78945
num = n
count = 0

# while num > 0:
#     count += 1
#     num = num//10
# print (count)


# Different approach of counting the digits
from math import *
def count_digit(num):
    return int(log10(num) + 1)
print(count_digit(num))