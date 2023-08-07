# [필수] 배치하기

N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
arr2 = list(map(int, input().split()))
arr2.sort(reverse=True)

sum = 0
for i in range(N):
	sum += arr1[i]*arr2[i]
print(sum)