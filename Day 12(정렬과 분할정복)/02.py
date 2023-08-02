# 과정 출력하기 (삽입)

n = int(input())
arr = list(map(int, input().split()))
print(" ".join(map(str, arr)))

for i in range(1, n):
	for j in range(i , 0, -1):
		if(arr[j] < arr[j-1]):
			tmp = arr[j]
			arr[j] = arr[j-1]
			arr[j-1] = tmp
			print(" ".join(map(str, arr)))