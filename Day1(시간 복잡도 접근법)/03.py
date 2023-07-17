# [필수] 수 정렬하기

N = int(input())  
numbers = [] 

for _ in range(N):
    num = int(input())
    numbers.append(num)

numbers.sort()

for num in numbers:
    print(num)