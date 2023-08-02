# 과정 출력하기 (버블)

n = int(input())
arr = list(map(int, input().split()))
print(" ".join(map(str, arr)))

for i in range(n-1):
	for j in range(n-i-1):
		if(arr[j] > arr[j+1]):
			tmp = arr[j+1]
			arr[j+1] = arr[j]
			arr[j] = tmp
			print(" ".join(map(str, arr)))
	