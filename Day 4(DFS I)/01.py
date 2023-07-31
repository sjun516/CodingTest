# 모든 순열

# for문을 돌려서 할 수는 있지만
# N중 for문을 돌려야 하므로 dfs를 쓰면 된다

def dfs(x):
	if(x == num): # 자릿수 다 찼다면 출력 배열 출력
		sen = ""
		for j in range(num):
			sen += str(arr[j]) + " " 
		print(sen)
		return 
	for i in range(num): # 1, 2, 3 중 하나를 고르기 위함
		if(chk[i] == i+1): # 앞에서 골랐으면 못 고름
			continue
		chk[i] = i+1 # 체크 배열에 수 입력
		arr[x] = i+1 # 출력 배열에 수 입력
		# print(arr[x])
		dfs(x+1) # 다음 자리 찾기
		chk[i] = 0 # 다음 탐색에 영향 안미치려고

num = int(input())
arr = [0]*num
chk = [0]*num
dfs(0)
		
		