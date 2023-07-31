# [필수] N과 M 2

# 내 코드

def dfs(x):
	if(x == b):
		sen = ""
		for j in range(b):
			sen += str(arr[j]) + " " 
		print(sen)
		return 
	for i in range(a):
		if(chk[i] == i+1): # 앞에서 골랐으면 못 고름
			continue
		cnt = 0
		for k in range(a): # 앞에서 고른게 큰수면 break
			if(chk[k] > i):
				cnt = 1
				break
		if(cnt == 1):
			continue
		chk[i] = i+1 # 체크 배열에 수 입력
		arr[x] = i+1 # 출력 배열에 수 입력
		# print(arr[x])
		dfs(x+1) # 다음 자리 찾기
		chk[i] = 0 # 다음 탐색에 영향 안미치려고

a, b = map(int, input().split())
arr = [0]*b
chk = [0]*a
dfs(0)

# 풀이 1

# def dfs(x):
# 	if(x == b):
# 		sen = ""
# 		for j in range(b):
# 			sen += str(arr[j]) + " " 
# 		print(sen)
# 		return 
# 	for i in range(arr[x-1]+1, a+1): # 1부터 시작
# 		arr[x] = i # 출력 배열에 수 입력
# 		# print(arr[x])
# 		dfs(x+1) # 다음 자리 찾기
# 		arr[x] = 0

# a, b = map(int, input().split())
# arr = [0]*b
# dfs(0)

# 풀이 2

# def dfs(x, y):
# 	if(x == b):
# 		sen = ""
# 		for j in range(b):
# 			sen += str(arr[j]) + " " 
# 		print(sen)
# 		return 
# 	for i in range(y, a+1):
# 		arr[x] = i # 출력 배열에 수 입력
# 		# print(arr[x])
# 		dfs(x+1, i+1) # 다음 자리 찾기
# 		arr[x] = 0

# a, b = map(int, input().split())
# arr = [0]*b
# dfs(0, 1)