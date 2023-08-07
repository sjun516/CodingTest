# 2xn 타일링 2

n = int(input())
arr = [0 for _ in range(1001)]
arr[1] = 1
arr[2] = 3
for i in range(3, n+1):
	arr[i] = arr[i-2]*2 + arr[i-1]
print(arr[n] % 10007)