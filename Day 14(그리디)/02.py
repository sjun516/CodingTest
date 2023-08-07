# [필수] 체육대회

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()

index = 0
cnt = 0
for num in arr2:
	if(num > arr1[index]):
		cnt += 1
		index += 1
print(cnt)
