# [필수] 나무 자르기

N, M = map(int, input().split())
arr = list(map(int, input().split()))
small = 0
big = 1000000000
answer = 0

while(small <= big):
	middle = (small + big) // 2
	
	tree = 0
	for i in range(N):
		if(arr[i] - middle > 0):
			tree += arr[i] - middle
	if(tree < M):
		big = middle - 1
	else:
		answer = middle
		small = middle + 1
		
print(answer)