# [필수] 약수의 합

import math

num = int(input(""))

sum = 0
for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        if i != num / i:
            sum += i + num / i
        else:
            sum += i

print(int(sum))