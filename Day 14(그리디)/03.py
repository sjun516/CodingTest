# [필수] 밧줄

N = int(input())
arr = []
for _ in range(N):
	arr.append(int(input()))
arr.sort()

arr2 = []
sum = 0
for i in range(N):
	arr2.append(arr[i] * (N-i))
arr2.sort(reverse=True)
print(arr2[0])