# [필수] 분수 비교하기

arr = list(map(int, input().split()))

num1 = arr[1] * arr[3]
a = num1//arr[1] 
b = num1//arr[3] 

if arr[0]*a > arr[2]*b:
    print("A/B")
elif arr[0]*a < arr[2]*b:
    print("C/D")
else:
    print("EQUALS")

