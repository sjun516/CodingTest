# 수 찾기

from bisect import bisect_left, bisect_right 

N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(M):
	index = bisect_left(arr1, arr2[i])
	if(index == N or arr1[index] != arr2[i]):
		print(0)
	else:
		print(1)


# N, M = map(int, input().split())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))

# def check(arr, num):
# 	l = 0
# 	r = len(arr) - 1
	
# 	while(l <= r):
# 		m = (l + r) // 2
# 		if(arr[m] > num):
# 			r = m - 1
# 		elif(arr[m] < num):
# 			l = m + 1
# 		else:
# 			return 1
# 	return 0

# for i in range(M):
# 	print(check(arr1, arr2[i]))
	
