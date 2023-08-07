# 2xn 타일링

# 피보나치 재귀 -> O(2의 n승)
# 피보나치 반복 -> O(n)

n = int(input())
arr = [0 for _ in range(1000+1)]
arr[1] = 1
arr[2] = 2
for i in range(3, n+1):
	arr[i] = arr[i-1] + arr[i-2]

print(arr[n] % 10007)