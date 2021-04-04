# import math
# x = int(input())
# print(math.factorial(x))

n = int(input())
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)